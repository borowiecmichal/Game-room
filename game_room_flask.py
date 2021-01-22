from flask import Flask, request
import random

def throw(cube_walls=6):
    return random.randint(1, cube_walls)

available_dices = (3, 4, 6, 8, 10, 12, 20, 100)

app = Flask(__name__)


@app.route('/game_room', methods=['POST', 'GET'])
def game_room():
    if request.method == 'GET':
        html = f"""
        <p>Welcome!</p>
        <p>To throw dices, check the type in areas below.</p>
        <form method='POST'>
            <input type="hidden" value={0} name="score_user">
            <input type="hidden" value={0} name="score_comp">
            <select name="size_1">
                <option value="3">D3</option>
                <option value="4">D4</option>
                <option value="6" selected>D6</option>
                <option value="8">D8</option>
                <option value="10">D10</option>
                <option value="12">D12</option>
                <option value="20">D20</option>
                <option value="100">D100</option>
            </select>
            <select name="size_2">
                <option value="3">D3</option>
                <option value="4">D4</option>
                <option value="6" selected>D6</option>
                <option value="8">D8</option>
                <option value="10">D10</option>
                <option value="12">D12</option>
                <option value="20">D20</option>
                <option value="100">D100</option>
            </select>
            <input type="submit" value="SEND">        
        </form>
        """
        return html
    else:
        user_first_shot = throw(int(request.form["size_1"]))
        user_second_shot = throw(int(request.form["size_2"]))
        comp_first_shot = throw(available_dices[random.randint(0,len(available_dices)-1)])
        comp_second_shot = throw(available_dices[random.randint(0,len(available_dices)-1)])
        user_round = user_first_shot + user_second_shot
        comp_round = comp_first_shot + comp_second_shot

        score_user = int(request.form["score_user"]) + user_round
        score_comp = int(request.form["score_comp"]) + comp_round
        html = f"""
        <p>Your dices went {user_first_shot} and {user_second_shot}. Your score is{score_user}</p>
        <p>Yours opponent dices went {comp_first_shot} and {comp_second_shot}. Yours opponent score is{score_comp}</p>
        <form method='POST'>
            <input type="hidden" value={score_user} name="score_user">
            <input type="hidden" value={score_comp} name="score_comp">
            <select name="size_1">
                <option value="3">D3</option>
                <option value="4">D4</option>
                <option value="6" selected>D6</option>
                <option value="8">D8</option>
                <option value="10">D10</option>
                <option value="12">D12</option>
                <option value="20">D20</option>
                <option value="100">D100</option>
            </select>
            <select name="size_2">
                <option value="3">D3</option>
                <option value="4">D4</option>
                <option value="6" selected>D6</option>
                <option value="8">D8</option>
                <option value="10">D10</option>
                <option value="12">D12</option>
                <option value="20">D20</option>
                <option value="100">D100</option>
            </select>
            <input type="submit" value="SEND">        
        </form>
        """
        return html

if __name__ == '__main__':
    app.run()
