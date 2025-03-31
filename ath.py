
app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template
app = Flask(__name__)


STUDENT_NAME = "Seyedmohammad Moeinishokouh"
mycloude = "gitttttttt"

def finalscore(athletic):
    score = []
    for i in range(4,9):
        score.append(float(athletic[i]))
    f_score = (sum(score) - (max(score)+min(score)))/3
    return f_score

def calculate_results():
    with open('athletes_score.txt','r') as athletes:
        max_score = 0
        country_score = {}
        country_list = []

        for athletic in athletes.readlines():
            athletic = athletic.strip().split()
            score = finalscore(athletic)

            if score > max_score and athletic[2] == 'F':
                winner = athletic
                max_score = score


def main():

            if athletic[3] in country_score:
                country_score[athletic[3]] += score
            else:
                country_score[athletic[3]] = score

            winner_result = f"{winner[0]} {winner[1]}, {winner[3]} - score: {max_score:.1f}"
        
            for country, C_score in country_score.items():
                country_list.append([C_score, country])
                country_list.sort(reverse=True)

            ranking = []
            for j in range(min(3, len(country_list))):
             ranking.append(f"{j+1}) {country_list[j][1]} - Total Score : {country_list[j][0]:.1f}")

            return winner_result, ranking

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run_script():
    winner, ranking = calculate_results()
    return render_template('result.html', winner=winner, ranking=ranking)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

