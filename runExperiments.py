import os, sys

sys.path.append(r'{}\EMAworkbench'.format(os.getcwd()))

from gr4spModel import getModel
from datetime import date

if __name__ == '__main__':
    '''
    Setup EMA Uncertainties, Levers and Outcomes
    '''
    model = getModel()

    '''
    Run EMA
    '''

    from EMAworkbench.ema_workbench import (SequentialEvaluator, MultiprocessingEvaluator, ema_logging, perform_experiments)
    from EMAworkbench.ema_workbench.em_framework.evaluators import (MC, LHS, FAST, FF, PFF, SOBOL, MORRIS)

    ema_logging.log_to_stderr(ema_logging.INFO)

    with MultiprocessingEvaluator(model) as evaluator:

        ## EET
        # results = evaluator.perform_experiments(scenarios=0, policies=15, levers_sampling=MORRIS) #levers + 1 * policies

        ## Variance-based SA
        # results = evaluator.perform_experiments(scenarios=0, policies=1050, levers_sampling=SOBOL)

        #Testing
        results = evaluator.perform_experiments(scenarios=0, policies=2)

    '''
    Print Results
    '''

    experiments, outcomes = results
    print(experiments.shape)
    print(list(outcomes.keys()))

    '''
    Save Results
    '''

    # Month abbreviation, day and year
    today = date.today()
    datekey = today.strftime("%Y-%b-%d")
    from ema_workbench import save_results

    save_results(results, r'./data/gr4sp_' + datekey + '.tar.gz')
