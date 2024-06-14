from sklearn import tree
clf = tree.DecisionTreeClassifier()

X = [[20, 50000, 1], [25, 70000, 0], [30, 90000, 1], [35, 120000, 0], [40, 150000, 1], [45, 180000, 0], [50, 200000, 1], [55, 220000, 0], [60, 250000, 1], [65, 280000, 0]]
y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

clf = clf.fit(X, y)

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
student = int(input("Are you a student? (1 for yes, 0 for no): "))

prediction = clf.predict([[age, income, student]])

if prediction[0] == 1:
    print("Based on the information you provided, you should buy a computer.")
else:
    print("Based on the information you provided, you should not buy a computer.")
