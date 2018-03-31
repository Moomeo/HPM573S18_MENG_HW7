import CalibrationClasses as CalibClasses
import CalibrationSettings as CalibSets
import scr.FigureSupport as Fig

# create a calibration object
calibration = CalibClasses.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# create the histogram of the resampled mortality probabilities
Fig.graph_histogram(
    observations=calibration.get_mortality_resamples(),
    title='Histogram of Resampled Mortality Probabilities',
    x_label='Mortality Probability',
    y_label='Counts')

# Estimate of mortality probability and the posterior interval
print('Estimate of mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))
