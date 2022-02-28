#
from pyomo.environ import *
model = ConcreteModel()

# 定义： 决策变量x、y
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

# 定义： 目标函数
model.profit = Objective(expr=40*model.x + 30*model.y, sense=maximize)

# 定义： 约束条件
model.demand = Constraint(expr= model.x <= 40)
model.laborA = Constraint(expr= model.x + model.y <= 80)
model.laborB = Constraint(expr= 2*model.x + model.y <= 100)

model.pprint()

SolverFactory('glpk', executable='/usr/bin/glpsol').solve(model).write()

# 输出结果
print('\nProfit = ', model.profit())

print('\nDecision Variables')
print('x = ', model.x())
print('y = ', model.y())

print('\nConstraints')
print('Demand  = ', model.demand())
print('Labor A = ', model.laborA())
print('Labor B = ', model.laborB())
