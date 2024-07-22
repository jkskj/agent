# -*- coding: utf-8 -*-
"""A simple example for conversation between user and assistant agent."""
import agentscope
from agentscope.agents import DialogAgent
from agentscope.agents.user_agent import UserAgent
from agentscope.pipelines.functional import sequentialpipeline


def main() -> None:
    """A basic conversation demo"""

    # 加载模型配置
    agentscope.init(model_configs="./configs/model_configs.json")
    host_sys_prompt = """

– 游戏开始，告诉用户游戏规则，并让用户选择汤底类型“1-红汤：指有死亡情节的汤；2-清汤：指没人死亡的汤；3-本格：指没有超自然现象；4-变格：指有超自然现象（灵异、科幻、超能力、妖怪等）”

– 用户选择完汤底类型，你会给出汤面，并告知用户有几轮提问机会，让用户开始推理并提问

– 根据用户的回答，判断用户所说与汤底是否相符，若相符则回答“是”、不符则回答“否”、若与事件不相关则回答”与此无关

– 每次回答“是”、“否”、或“与此无关”后，还要告知用户剩余提问轮数。

举例： 是。 你还剩下3轮提问机会。

– 若用户知晓汤底，可以让用户「回复」“还原事件“，并开始回答，你需要根据用户的回答来判断与汤底的一致性，并对用户回答完整程度进行评分，满分为10分

– 由你根据汤底的难度决定用户回答轮次的限制轮数，在超过限定轮数后你需要告知用户“游戏失败”，若用户没有给出答案，则将汤底告知用户

– 用户还原真相后，不用再提示剩余回答轮数，给出评分以及汤底，再询问用户是否继续游戏，如：“回复1-继续游戏”
"""

    # 创建对话Agent和用户Agent
    dialog_agent = DialogAgent(
        "host",
        model_config_name="glm-4",
        sys_prompt=host_sys_prompt,
        use_memory=True,
    )
    user_agent = UserAgent()

    # start the conversation between user and assistant
    x = None
    while x is None or x.content != "exit":
        x = sequentialpipeline([dialog_agent, user_agent], x)


if __name__ == "__main__":
    main()
