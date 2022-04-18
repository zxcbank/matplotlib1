from matplotlib import pyplot as plt

subjects = ['лит','био', 'анг', 'рус','фра','хим','инф','ист', 'обж', 'общ', 'фл','физ','геом']
marks = [2.36, 2.47, 3.17, 3.20, 3.20,3.33, 3.33, 3.64, 3.67, 3.76, 4.0, 4.21, 4.50]
plt.plot(subjects, marks, color = 'green', marker = 'o',linestyle = 'solid')
plt.title('Средние баллы 18.04.2022 (10кл)')
plt.ylabel("AVERAGE MARK")
plt.show()
