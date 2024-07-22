import agentscope
from agentscope.agents import ReActAgent
from agentscope.agents.user_agent import UserAgent
from agentscope.pipelines.functional import sequentialpipeline
from agentscope.service import ServiceToolkit, read_json_file, ServiceResponse, ServiceExecStatus
from zhipuai import ZhipuAI


def zhipuai_text_to_image(
        prompt: str,
        api_key: str,
) -> ServiceResponse:
    """Generate a image based on the given prompt, and return a image url.

    Args:
        prompt (`str`):
            The text prompt to generate image.
        api_key (`str`):
            The api key for the zhipuai api.

    Returns:
        ServiceResponse:
        A dictionary with two variables: `status` and`content`.
        If `status` is ServiceExecStatus.SUCCESS,
        the `content` is a str with key 'fig_path" and
        value is  the path to the generated images.

    Example:

        .. code-block:: python

            prompt = "A beautiful sunset in the mountains"
            print(dashscope_text_to_image(prompt, "{api_key}"))

    > {
    >     'status': 'SUCCESS',
    >     'content': {'image_url': 'IMAGE_URL1'}
    > }

    """
    try:
        client = ZhipuAI(api_key=api_key)  # 请填写您自己的APIKey

        response = client.images.generations(
            model="cogview-3",  # 填写需要调用的模型名称
            prompt=prompt,
        )

        url = response.data[0].url

        # save images to save_dir
        if url is not None:
            # Return the web urls
            return ServiceResponse(
                ServiceExecStatus.SUCCESS,
                {"image_url": url},
            )
        else:
            return ServiceResponse(
                ServiceExecStatus.ERROR,
                "Error: Failed to generate images",
            )
    except Exception as e:
        return ServiceResponse(
            ServiceExecStatus.ERROR,
            str(e),
        )


def main() -> None:
    """A basic conversation demo"""

    # 加载模型配置
    agentscope.init(model_configs="./configs/model_configs.json")
    # 初始化一个ServiceToolkit对象并注册服务函数及其必要参数
    service_toolkit = ServiceToolkit()
    service_toolkit.add(
        read_json_file,
    )
    service_toolkit.add(
        zhipuai_text_to_image,
        api_key="********"
    )
    print(service_toolkit.tools_instruction)
    # 创建对话Agent和用户Agent
    dialog_agent = ReActAgent(
        "assistant",
        model_config_name="glm-4",
        service_toolkit=service_toolkit,
        sys_prompt="你是一个助手，帮助用户解决问题",
        use_memory=True,
    )
    user_agent = UserAgent()

    # start the conversation between user and assistant
    x = None
    while x is None or x.content != "exit":
        x = sequentialpipeline([dialog_agent, user_agent], x)


if __name__ == "__main__":
    main()
