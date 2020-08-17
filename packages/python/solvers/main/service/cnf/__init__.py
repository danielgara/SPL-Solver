import pysat.formula as formulas
import pysat.solvers as solvers
import solvers.main.service.cnf.feature_model as feature_model


solver_map = {
    "cadical": solvers.Cadical,
    "glucose_3": solvers.Glucose3,
    "glucose_4": solvers.Glucose4,
    "lingeling": solvers.Lingeling,
    "maple_chrono": solvers.MapleChrono,
    "maple_cm": solvers.MapleCM,
    "maple_sat": solvers.Maplesat,
    "minicard": solvers.Minicard,
    "minisat_22": solvers.Minisat22,
    "minista_gh": solvers.MinisatGH,
}


def get_formula(statements, restrictions):
    clauses = statements + restrictions

    return formulas.CNF(from_clauses=clauses)


def get_solutions(formula, solver, num_solutions):
    solutions = []

    with solver(bootstrap_with=formula.clauses) as solver:
        for index, solution in enumerate(solver.enum_models()):
            if index >= num_solutions:
                return solutions

            solutions.append(solution)

    return solutions
