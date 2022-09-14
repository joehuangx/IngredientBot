#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for InSeason

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_InSeason = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_fruit":["火龍果"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_InSeason:
        print("[InSeason] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT, all_utt):
    debugInfo(inputSTR, utterance)
    
    resultDICT["inseason"] = True

    if utterance == "[現在][該]吃哪些[水果]？":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[2]

    if utterance == "[現在]有什麼":
        resultDICT["time"] = args[0]

    if utterance == "[現在]有什麼[水果][好吃]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[現在]有什麼[當季][食材]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[2]

    if utterance == "[現在]有甚麼[好吃]的[當季][水果]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[3]

    if utterance == "[現在]有甚麼[海鮮]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[現在]有甚麼[當季][水果][好吃]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[2]

    if utterance == "[現在當季]的[水果]是什麼":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "[目前]盛產甚麼[水果]":
        resultDICT["time"] = args[0]
        resultDICT["type"] = args[1]

    if utterance == "告訴[我][現在]有什麼[當季][食材]":
        resultDICT["time"] = args[1]
        resultDICT["type"] = args[3]

    if utterance == "有什麼[水果]":
        if args[0] not in ["蔬菜", "水果", "海鮮", "食材"]:
            resultDICT.pop("inseason")
        else:
            resultDICT["type"] = args[0]

    if utterance == "有什麼[當季][食材]":
        resultDICT["type"] = args[1]

    if utterance == "[現在]盛產什麼":
        resultDICT["time"] = args[0]

    if utterance == "推薦[一個][食材]":
        resultDICT["type"] = args[1]

    if utterance == "推薦什麼[食材]":
        resultDICT["type"] = args[0]

    if utterance == "[9月]的[食材]":
        if "現在" in args[0] or "當季" in args[0] or "當令" in args[0] or "幾月" in args[0] or args[1] in ["料理", "早餐", "午餐", "晚餐"]:
            resultDICT.pop("inseason")
        else:
            resultDICT["time"] = args[0]
            resultDICT["type"] = args[1]

    if utterance == "[秋天][可以]吃什麼":
        if "今天" in args[0]:
            resultDICT.pop("inseason")
        else:
            resultDICT["time"] = args[0]

    return resultDICT