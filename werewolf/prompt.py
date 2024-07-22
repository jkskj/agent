# -*- coding: utf-8 -*-
"""Used to record prompts, will be replaced by configuration"""
from agentscope.parsers.json_object_parser import MarkdownJsonDictParser


class Prompts:
    """Prompts for werewolf game"""

    to_wolves = (
        "{}，如果你是唯一的狼人，消灭一个玩家。否则，"
        "与你的队友讨论并达成协议。"
    )

    wolves_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考要消灭哪一个玩家",
            "speak": "说明要消灭哪一个玩家并解释原因",
            "finish_discussion": "讨论是否达成一致(true/false)",
        },
        required_keys=["thought", "speak", "finish_discussion"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata=["finish_discussion"],
    )

    to_wolves_vote = "你投票要淘汰哪位玩家？"

    wolves_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考要淘汰哪位玩家",
            "vote": "玩家姓名",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    to_wolves_res = "得票最多的玩家是{}。"

    to_witch_resurrect = (
        "{witch_name}，你是女巫。今晚{dead_name}被淘汰。你想要复活{dead_name}吗？"
    )

    to_witch_resurrect_no = "女巫选择不复活玩家。"
    to_witch_resurrect_yes = "女巫选择复活玩家。"

    witch_resurrect_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考是否复活淘汰的玩家",
            "speak": "说想说的",
            "resurrect": "是否复活玩家，请和说出的话一致(true/false)",
        },
        required_keys=["thought", "speak", "resurrect"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata=["resurrect"],
    )

    to_witch_poison = (
        "你想淘汰一名玩家吗？如果是，"
        "指定姓名。"
    )

    witch_poison_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考是否淘汰一名玩家",
            "speak": "说想说的",
            "eliminate": "是否淘汰一名玩家，请和说出的话一致(true/false)",
        },
        required_keys=["thought", "speak", "eliminate"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata=["eliminate"],
    )

    to_seer = (
        "{}, 你是预言家。今晚你想要查验{}中的哪位玩家?"
    )

    seer_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考想要查验哪位玩家",
            "speak": "玩家姓名",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    to_seer_result = "好的，{}的角色是{}。"

    to_all_danger = (
        "白天来临，所有玩家睁开眼睛。昨夜，以下玩家被淘汰：{}。"
    )

    to_all_peace = (
        "白天来临，所有玩家睁开眼睛。昨夜是平安夜，没有玩家被淘汰。"
    )

    to_all_discuss = (
        "现在活着的玩家是{}。根据游戏规则和你的角色，基于现状和你获得的信息，为了赢得游戏，在活着的玩家中投票淘汰一名玩家，你想对其他人说些什么？你可以决定是否揭露你的角色。"
    )

    survivors_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "思考要淘汰哪名玩家",
            "speak": "说想说的",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    to_all_dis = (
        "{}的发言是:{}"
    )

    survivors_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "综合所有发言,思考要淘汰哪名玩家",
            "vote": "玩家姓名",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    to_all_vote = (
        "现在活着的玩家是{}。根据游戏规则和你的角色，基于现状和你获得的信息，为了赢得游戏，在活着的玩家中投票淘汰一名你认为是狼人的玩家。"
    )

    to_all_res = "{}被投票淘汰了。"

    to_all_wolf_win = (
        "狼人获胜，接管了村庄。祝你下次好运！"
    )

    to_all_village_win = (
        "游戏结束。狼人被击败，村庄再次安全了！"
    )

    to_all_continue = "游戏继续。"
