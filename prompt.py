from agentscope.parsers import MarkdownJsonDictParser


class Prompts:
    judge_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考相似的两个词语",
            "speak": "说出两个词语",
            "object1": "第一个词语",
            "object2": "第二个词语",
        },
        required_keys=["thought", "speak", "object1", "object2"],
        keys_to_content="speak",
        keys_to_metadata=["object1", "object2"],
    )
    to_player = "你的词语是{}。"

    to_start = "游戏开始！！！"

    to_all_describe = (
        "现在在场的玩家是{}，请按顺序描述你的词语。"
    )
    to_all_dis = (
        "{}的发言是:{}"
    )

    to_all_vote = (
        "现在在场的玩家是{}，根据游戏规则和你的词语，基于现状和你获得的信息，为了赢得游戏，请淘汰一名认为是卧底的玩家。"
    )

    survivors_describe_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "怎样描述自己的词语不会被人淘汰",
            "speak": "说想说的",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    survivors_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "综合所有发言,思考谁是卧底",
            "vote": "玩家姓名",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )
    to_all_res = "{}被投票淘汰了。"

    to_all_wolf_win = (
        "游戏结束。卧底胜利！"
    )

    to_all_village_win = (
        "游戏结束。卧底被淘汰了！"
    )

    to_all_continue = "游戏继续。"
