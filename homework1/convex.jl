using JuMP, GLPK
m = Model(GLPK.Optimizer)
@variable(m, x[1:5] >= 0, integer = true)
@objective(m, Min, 0.1x[2] + 0.2x[3] + 0.3x[4] + 0.8x[5])
@constraint(m, constraint1, x[1] + 2x[2] + x[4] == 100)
@constraint(m, constraint2, 2x[3] + 2x[4] + x[5] == 100)
@constraint(m, constraint3, 3x[1] + x[2] + 2x[3] + 3x[5] == 100)
#print(m)
JuMP.optimize!(m)
#println("Optimal Soutions:")
for i in 1:5
    println("x$i = ", JuMP.value(x[i]))
end
println("z = ", JuMP.objective_value(m))
