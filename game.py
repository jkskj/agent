import random
from functools import partial

import agentscope
from agentscope import msghub
from agentscope.message import Msg
from agentscope.pipelines import sequentialpipeline

from prompt import Prompts
from utils import set_parsers, extract_name_and_id, n2s, majority_vote, check_winning, update_alive_players


def main() -> None:
    """game"""
    # default settings
    HostMsg = partial(Msg, name="Moderator", role="assistant", echo=True)
    # read model and agent configs, and initialize agents automatically
    agents = agentscope.init(
        model_configs="./configs/model_configs.json",
        agent_configs="./configs/agent_configs.json",
        project="game",
    )
    judge = agents[0]
    survivors = agents[1:]
    a, b = survivors[:3], survivors[3:]
    categories = ["运动类", "电器类", "家居类", "蔬菜类", "动物类", "水果类"]
    content = random.choice(categories)
    hint = HostMsg(content=content)
    set_parsers(judge, Prompts.judge_parser)
    meta = judge(hint).metadata
    object1 = meta.get("object1", "苹果")
    object2 = meta.get("object2", "香蕉")
    hint = HostMsg(content=Prompts.to_player.format(object1))
    for o in a:
        o.observe(hint)
    hint = HostMsg(content=Prompts.to_player.format(object2))
    for o in b:
        o.observe(hint)
    # start the game
    hint = HostMsg(content=Prompts.to_start)
    with msghub(survivors, announcement=hint) as hub:
        for _ in range(1, 4):
            # describe
            set_parsers(survivors, Prompts.survivors_describe_parser)
            for survivor in survivors:
                content = survivor().content
                msg = HostMsg(content=Prompts.to_all_dis.format(survivor.name, content))
                hub.broadcast(msg)

            # vote
            set_parsers(survivors, Prompts.survivors_vote_parser)
            hint = HostMsg(content=Prompts.to_all_vote.format(n2s(survivors)))
            votes = [
                extract_name_and_id(_(hint).content)[0] for _ in survivors
            ]
            vote_res = majority_vote(votes)
            # broadcast the result to all players
            result = HostMsg(content=Prompts.to_all_res.format(vote_res))
            hub.broadcast(result)

            survivors, b = update_alive_players(
                survivors,
                b,
                vote_res,
            )

            if check_winning(survivors, b, "Moderator"):
                break

            hub.broadcast(HostMsg(content=Prompts.to_all_continue))


if __name__ == "__main__":
    main()
