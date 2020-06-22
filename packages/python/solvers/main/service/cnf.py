import pysat.formula as formulas
import pysat.solvers as solvers


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


def get_formula(statement):
    return formulas.CNF(from_string=statement)


def is_satisfiable(formula, solver):
    with solver(bootstrap_with=formula.clauses) as solver:
        return solver.solve()


def get_solutions(formula, solver):
    with solver(bootstrap_with=formula.clauses) as solver:
        return [
            solution for index, solution in enumerate(solver.enum_models())
        ]
