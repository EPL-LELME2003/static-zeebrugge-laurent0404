import pyomo.environ as pyo
#laulau
#hello word it's me !

# Create a Pyomo model
model = pyo.ConcreteModel()


# Define model parameters
##########################################
############ CODE TO ADD HERE ############
##########################################
LHV_NH3 = 18.5e6
LHV_CH4 = 50e6

rho_NH3 = 600
rho_CH4 = 500

losses_NH3 = 0.4
losses_CH4 = 0.35

boat_capacity = 2e5

H2_CH4 = 0.25
CO2_CH4 = 2.75
H2_NH3 = 0.18
# Define model variables
##########################################
############ CODE TO ADD HERE ############
##########################################

model.boat_NH3 = pyo.Var(within = pyo.NonNegativeReals, bounds = 
(0,100))

model.boat_CH4 = pyo.Var(within = pyo.NonNegativeIntegers, bounds = 
(0,100))

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

model.obj = pyo.Objective(expr = (rho_CH4*model.boat_CH4*H2_CH4 + rho_NH3*model.boat_NH3*H2_NH3)*boat_capacity, sense = pyo.maximize) 
# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

model.con1 = pyo.Constraint(expr = (model.boat_NH3 + model.boat_CH4 <= 100))

model.con2 = pyo.Constraint(expr = ((rho_CH4*model.boat_CH4*LHV_CH4/losses_CH4 + rho_NH3*model.boat_NH3*LHV_NH3/losses_NH3)*boat_capacity<= 140e12))

model.con3 = pyo.Constraint(expr = (boat_capacity*rho_CH4*model.boat_CH4*CO2_CH4<= 14e6) )   

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory("C:/Users/ljacq/gurobi.lic")
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################
print(pyo.check_optimal_termination(sol)) 
