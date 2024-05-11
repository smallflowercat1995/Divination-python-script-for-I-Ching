
"""周易算卦 思路
    基本定义：0 阴爻 '--  --', 1 阳爻 '------'
    启动用户界面
    从json格式文件 history.json 加载历史算卦问题记录的函数
    输出历史占卜结果
    用户问询算卦问题
    抛三枚硬币来决定每一爻的阴阳
    创建六爻卦象图
    输出卦象图(代码里会用 0 1 组成进行记录卦象图结果)，每一爻命名(每爻通过阴阳代码和序号组成标记用于查爻题)，格式代码组成如下

        ```卦爻命名，阴阳代码和序号组成输出思路示例
        (06)代表 上六爻：--  --
        (15)代表 九五爻：------
        (04)代表 六四爻：--  --
        (03)代表 六三爻：--  --
        (12)代表 九二爻：------
        (01)代表 初六爻：--  --
        [06,15,04,03,12,01]
        ```
        ```卦象，阴阳代码里会用 0 1 组成进行记录输出示例
        --  --
        ------
        --  --
        --  --
        ------
        --  --
        [0,1,0,0,1,0]
        ```
    针对每爻通过阴阳代码和序号组成标记(比如 [06,15,04,03,12,01])从 yao.json 文件中查找对应的爻题、爻辞和爻辞白话解释,输出格式如下
        ```每爻格式输出
        上六爻(06)：--  --
            爻题：爻题内容
            爻辞：爻辞内容
            爻辞白话解释：爻辞白话解释内容
        九五爻(15)：------
            爻题：爻题内容
            爻辞：爻辞内容
            爻辞白话解释：爻辞白话解释内容
        六四爻(04)：--  --
            爻题：爻题内容
            爻辞：爻辞内容
            爻辞白话解释：爻辞白话解释内容
        六三爻(03)：--  --
            爻题：爻题内容
            爻辞：爻辞内容
            爻辞白话解释：爻辞白话解释内容
        九二爻(12)：------
            爻题：爻题内容
            爻辞：爻辞内容
            爻辞白话解释：爻辞白话解释内容
        初六爻(01)：--  --
            爻题：爻题内容
            爻辞：爻辞内容
            爻辞白话解释：爻辞白话解释内容
        ```

    根据对应的阴阳 0 1 组成代码(比如 [0,1,0,0,1,0])从 hexagram.json 格式文件中查找卦名、卦辞、卦辞白话解释，输出格式如下
        ```卦格式输出
        --  --
        ------
        --  --
        --  --
        ------
        --  --
            卦名：卦名内容
            卦辞：卦辞内容
            卦辞白话解释：卦辞白话解释内容
        ```
    根据卦辞白话解释内同吉凶关键字输出用户问题成功的结果或概率，比如大吉90%、吉75%、凶25%、大凶0%和一般50%(无法判断则返回)

    存储输出的内容在每次占卜后将所有相关信息存储到历史记录文件 history.json 中。这将包括时间、问题、每一爻的爻题、爻辞、爻辞白话解释、卦名、卦辞、卦辞白话解释以及事成概率到json格式文件 history.json 文件，存储格式如下：
        ```历史文件内容格式
        [
            {
                "time": 2024-03-12 03:24:00,
                "question": "我应该接受这份工作吗？",
                "hexagram": [0, 1, 0, 0, 1, 0],
                "yao_info": {
                    "06": {"title": "爻题1", "text": "爻辞1", "interpretation": "爻辞白话解释1"},
                    "15": {"title": "爻题2", "text": "爻辞2", "interpretation": "爻辞白话解释2"},
                    "04": {"title": "爻题3", "text": "爻辞3", "interpretation": "爻辞白话解释3"},
                    "03": {"title": "爻题4", "text": "爻辞4", "interpretation": "爻辞白话解释4"},
                    "12": {"title": "爻题5", "text": "爻辞5", "interpretation": "爻辞白话解释5"},
                    "01": {"title": "爻题6", "text": "爻辞6", "interpretation": "爻辞白话解释6"}
                },
                "hexagram_info": {
                    "name": "卦名1",
                    "text": "卦辞1",
                    "interpretation": "卦辞白话解释1"
                },
                "prediction": "吉75%"
            }
        ]
        ```



代码参考素材：
```
https://yijing.5000yan.com/zhouyi/
https://zhuanlan.zhihu.com/p/377091070
八卦爻构成基本解释
    卦象：以阴阳爻表示，六个阳爻组成的乾卦，六根阴爻组成的坤卦等；
    卦名：每一卦都有一个特定的名称，如：屯、、蒙、未济等；
    卦辞：对卦的整体解释判断。如：《乾》卦的卦辞：“元亨，利贞。”
    爻题：对每一爻位置的命名。在《易经》里以“六”表示阴爻，以“九”表示阳爻，由下至上分别以“初、二、三、四、五、上”表示六根爻的位置。如：巽卦的“初六、九二、九三、六四、九五、上九”，这里要注意的是顺序一定不能错；
    爻辞：紧随爻题之后，对每一爻的解释和阐述。
古人在用揲蓍法布卦时，对占卜前的状态有近似宗教仪式般的“规矩”：
    1．占卜前一晚早睡，不做任何事。清晨早起头脑清醒、体力充沛是布卦的好时机。
    2．如厕后要洗手，饭后要漱口。
    3．晚上11点后不卜，因在两日交接之时，天地混沌未明，且精神疲倦。
    4．不可以玩笑或嬉戏的态度占卜。
    5．心未定不卜，心不诚不卜，赌博之事不卜，奸秽盗淫之事更不可卜。
    6．一事只一卜，不可反复请示。
    7．无事不要试卦。
    8．心意已决之事不卜，可凭借智慧做判断之事不卜。
    9．占卜的地方最好在干净整洁的书桌上。占卜时的思维不要受到外物的影响，所以不宜在闹市、卧室或厕所等环境中
"""
# -*- coding: utf-8 -*-
import os
import time
import json
import random
from datetime import datetime

# 定义阴爻和阳爻
YIN_YAO = 0
YANG_YAO = 1

# 定义爻的显示方式
DISPLAY_YAO = {
    YIN_YAO: '--  --',
    YANG_YAO: '------'
}

# 定义爻的名称
NAME_YAO = {
    YIN_YAO: '六',
    YANG_YAO: '九'
}

# 定义爻的位置
POSITION_YAO = ['初', '二', '三', '四', '五', '上']

# 加载历史算卦问题记录
def load_history():
    if os.path.exists('history.json'):
        with open('history.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
    else:
        history = []
    return history

# 输出历史占卜结果
def display_history(history):
    for record in history:
        print('--------占卜历史结果开始-------')
        print(record)
        print('--------占卜历史结果结束-------')

# 用户问询算卦问题
def ask_question():
    question = input("请输入你的问题：")
    return question

# 抛三枚硬币来决定每一爻的阴阳
def throw_coins():
    return random.choice([YIN_YAO, YANG_YAO])

# 创建六爻卦象图
def create_hexagram():
    hexagram = [throw_coins() for _ in range(6)]
    return hexagram
# 输出卦象图
def display_hexagram(hexagram):
    print('卦象')
    for i in range(5, -1, -1):
        print(DISPLAY_YAO[hexagram[i]])

# 针对每爻从json文件中查找对应的爻题、爻辞和爻辞白话解释
def lookup_yao(hexagram):
    yao_codes=[]
    with open('yao.json', 'r', encoding='utf-8') as f:
        yao_data = json.load(f)
    yao_infos = {}
    print('爻解')
    for i in range(5, -1, -1):
        yao_code = str(hexagram[i]) + str(i+1)
        yao_codes.append(yao_code)
        if yao_code in yao_data:
            yao_info = yao_data[yao_code]
            print(f"{POSITION_YAO[i]}{NAME_YAO[hexagram[i]]}爻({yao_code})：{DISPLAY_YAO[hexagram[i]]}")
            print(f"    爻题：{yao_info['title']}")
            print(f"    爻辞：{yao_info['text']}")
            print(f"    爻辞白话解释：{yao_info['interpretation']}")
            yao_infos[yao_code] = yao_info
        else:
            print(f"没有找到{yao_code}的信息")
    print(f"爻码：{yao_codes}")
    return yao_infos if yao_infos else None

# 根据对应的阴阳 0 1 组成代码从json格式文件中查找卦名、卦辞、卦辞白话解释
def lookup_hexagram(hexagram):
    with open('hexagram.json', 'r', encoding='utf-8') as f:
        hexagram_data = json.load(f)
    hexagram_code = ''.join(str(yao) for yao in hexagram)
    print('卦解')
    print(f"卦码：{hexagram_code}")
    if hexagram_code in hexagram_data:
        hexagram_info = hexagram_data[hexagram_code]
        print(f"卦名：{hexagram_info['name']}")
        print(f"卦辞：{hexagram_info['text']}")
        print(f"卦辞白话解释：{hexagram_info['interpretation']}")
    else:
        print(f"没有找到{hexagram_code}的信息")
    return hexagram_data[hexagram_code] if hexagram_code in hexagram_data else None

# 根据卦辞白话解释内同吉凶关键字输出用户问题成功的结果或概率
def predict_success(hexagram):
    with open('hexagram.json', 'r', encoding='utf-8') as f:
        hexagram_data = json.load(f)
    hexagram_code = ''.join(str(yao) for yao in hexagram)
    hexagram_info = hexagram_data[hexagram_code]
    interpretation = hexagram_info['text'] + ' ' + hexagram_info['interpretation']
    if '大凶' in interpretation:
        print("成事概率0%，大凶")
        return '成事概率0%，大凶'
    elif '凶' in interpretation:
        print("成事概率25%,凶")
        return '成事概率25%,凶'
    elif '吉' in interpretation:
        print("成事概率75%,吉")
        return '成事概率75%,吉'
    elif '大吉' in interpretation:
        print("成事概率90%,大吉")
        return '成事概率90%,大吉'
    else:
        print("成事概率50%,自行判断")
        return '成事概率50%,自行判断'


# 存储输出的内容在每次占卜后将所有相关信息存储到历史记录文件中
def store_history(question, hexagram, yao_info, hexagram_info, prediction):
    history = load_history()
    record = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'question': question,
        'hexagram': hexagram,
        'yao_info': {str(hexagram[i]) + str(i+1): yao_info.get(str(hexagram[i]) + str(i+1), {}) for i in range(6)} if yao_info else {},
        'hexagram_info': hexagram_info if hexagram_info else {},
        'prediction': prediction
    }
    history.append(record)
    with open('history.json', 'w',encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False)

# 主程序
def main():
    history = load_history()
    display_history(history)
    question = ask_question()
    hexagram = create_hexagram()
    display_hexagram(hexagram)
    yao_info = lookup_yao(hexagram)
    hexagram_info = lookup_hexagram(hexagram)
    prediction = predict_success(hexagram)
    store_history(question, hexagram, yao_info, hexagram_info, prediction)

# 执行
if __name__ == "__main__":
    main()
