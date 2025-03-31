# Write your solution here, DO NOT CREATE A NEW PROJECT
# WARNING: if you create a new project, your exam paper will not be collected
#                     and you will be required to attend the next exam session.
#
# WARNING: on Windows 10, (Italian keyboard) characters like [ ] { } must be
#                     created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# WARNING: on macOS, you must use CTRL-C and CTRL-V inside the virtual
#                     machine and NOT command-C command-V
#
# if your keyboard is damaged, you can use the mouse to copy/paste 
#                     special characters such as [ ] { } < > from this text.

STUDENT_NAME = "Seyedmohammad Moeinishokouh"
mycloude = "gitttttttt"
print("Exam of " + STUDENT_NAME)

# Write here your solution:

def finalscore(athletic):
    score = []
    for i in range(4,9):
        score.append(float(athletic[i]))
    f_score = (sum(score) - (max(score)+min(score)))/3
    return(f_score)


def main():
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
            if athletic[3] in country_score :
                country_score[athletic[3]] = country_score[athletic[3]] + score
            else :
                country_score[athletic[3]] = score
        print("Women's winner:\n%s %s,%s - score: %.1f\n" % (winner[0],winner[1],winner[3],max_score))
        for country , C_score in country_score.items():
            country_list.append([C_score,country])
        country_list.sort(reverse=True)
        print('Overall national ranking:')
        for j in range(3):
            print('%d) %s - Total Score : %.1f'%((j+1),country_list[j][1],country_list[j][0]))

main()