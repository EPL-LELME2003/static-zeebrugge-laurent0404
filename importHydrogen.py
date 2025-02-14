import pyomo.environ as pyo
#laulau
#hello word it's me !

# Create a Pyomo model
model = pyo.ConcreteModel()


# Define model parameters
##########################################
############ CODE TO ADD HERE ############
##########################################
model.LHV_NH3 = pyo.Param(initialize=18.5e6)
model.LHV_CH4 = pyo.Param(initialize=50e6)

model.rho_NH3 = pyo.Param(initialize=600)
model.rho_CH4 = pyo.Param(initialize=500)

model.losses_NH3 = pyo.Param(initialize=0.4)
model.losses_CH4 = pyo.Param(initialize=0.35)

model.boat_capacity = pyo.Param(initialize=2e5)
model.nbr_boat = pyo.Param(initialize=100)

model.H2_CH4 = pyo.Param(initialize=0.25)
model.CO2_CH4 = pyo.Param(initialize=2.75)
model.H2_NH3 = pyo.Param(initialize=0.18)
# Define model variables
##########################################
############ CODE TO ADD HERE ############
##########################################

model.boat_NH3 = pyo.Var(within = pyo.NonNegativeIntegers, bounds = (0,model.nbr_boat))

model.boat_CH4 = pyo.Var(within = pyo.NonNegativeIntegers, bounds = (0,model.nbr_boat))

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

model.obj = pyo.Objective(expr = (model.rho_CH4*model.boat_CH4*model.H2_CH4 + model.rho_NH3*model.boat_NH3*model.H2_NH3)*model.boat_capacity, sense = pyo.maximize) 
# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

model.con1 = pyo.Constraint(expr = (model.boat_NH3 + model.boat_CH4 <= 100))

model.con2 = pyo.Constraint(expr = ((model.rho_CH4*model.boat_CH4*model.LHV_CH4/(1-model.losses_CH4) + model.rho_NH3*model.boat_NH3*model.LHV_NH3/(1-model.losses_NH3))*model.boat_capacity <= 140e12*3600))

model.con3 = pyo.Constraint(expr = (model.boat_capacity*model.rho_CH4*model.boat_CH4*model.CO2_CH4 <= 14e6*1e3) )   

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory("gurobi")
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################
print(pyo.check_optimal_termination(sol)) 
print("Nombre de bateau de CH4 :", model.boat_CH4.value)
print("Nombre de bateau de NH3 :", model.boat_NH3.value)