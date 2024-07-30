import ollama
import glob
import os

def action_analyzer_prompt():
    prompt = """
You have the ability to analyze player actions from soccer match footage.
Watch the soccer match footage and analyze which of the actions listed below the player's actions correspond to.

The types of actions are as follows:

1. Pass
2. Shoot
3. Cross
4. Dribble
5. Successful Tackle
6. High Pass
7. Header
8. Others

Please output the corresponding action. Refer to the following example for output format.
===Example===
<output>
Shoot
===End of Example===

Let's begin!
<output>
"""

    return prompt

def get_response(img_path, prompt):
    response = ollama.chat(
        model = "llava",
        messages = [
            {
                "role": "user",
                "content": prompt,
                "content": [img_path]
            }
        ]
    )

    return response["message"]["content"]

def get_img_path_list(img_folder):
    img_path_list  = glob.glob(os.path.join(img_folder, '*'))
    img_path_list.sort()
    return img_path_list

def main():
    #* 対象ファイルのパス取得
    img_folder = "data/output/"
    img_path_list = get_img_path_list(img_folder)

    #* プロンプト設定
    prompt = action_analyzer_prompt()

    for i, img_path in enumerate(img_path_list):
        print(f"target path: {img_path}")
        response = get_response(img_path, prompt)
        print(f"Frame{i}: {response}")


if __name__ == "__main__":
    main()