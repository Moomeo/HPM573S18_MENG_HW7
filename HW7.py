# Homework 7
import scipy.stats as stat
import CalibrationClasses as CalibClasses
import CalibrationSettings as CalibSets
import CalibrationClasses6 as CalibClasses6
import CalibrationSettings6 as CalibSets6

# Problem 1
calibration1 = CalibClasses.Calibration()
calibration1.sample_posterior()
print("The percentage of survival over 5 years",calibration1.get_5yr_survival_percentage())

#problem 2
print('If the probability of 5-year survival is q,'
      'The number of participants that survived beyond 5 years in a cohort of N participants'
      'follows Binomial distribution. And the parameter is (K,N,q).')

#problesm3
likelihood = stat.binom.pmf(k=400, n=573, p =0.5, loc = 0)
print('The likelihood is:',likelihood)

#problem 4
#estimated annual mortality probability and the 95% credible interval
# create a calibration object
calibration = CalibClasses.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))

#problem 5
#Use the calibrated model to estimate the mean survival time of the cohort of size 1,000. Report the 95% projection interval.
# initialize a calibrated model
calibrated_model = CalibClasses.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))

#problem 6
# If a clinical study that reports 800 of 1146 participants survived at the end of the 5-year study period.
# create a calibration object
calibration6 = CalibClasses6.Calibration()
# sample the posterior of the mortality probability
calibration6.sample_posterior()
# Estimate of mortality probability and the posterior interval
print('Estimate of new mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets6.ALPHA, prec=0),
      calibration6.get_mortality_estimate_credible_interval(CalibSets6.ALPHA, 4))

# initialize a calibrated model
calibrated_model6 = CalibClasses6.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model6.simulate(CalibSets6.SIM_POP_SIZE, CalibSets6.TIME_STEPS)

# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets6.ALPHA, prec=0),
      calibrated_model6.get_mean_survival_time_proj_interval(CalibSets6.ALPHA, deci=4))

print("The credible interval of the estimated annual mortality probability, and the projection interval of the mean survival /"
      "time of the latter study is narrower than the former study. The latter model has a slight lower estimate mean mortality probabilty/"
      "While it still has a slight lower mean survival time")
