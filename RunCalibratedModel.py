import CalibrationClasses as CalibSupport
import CalibrationSettings as CalibSets
import scr.FigureSupport as Fig


# initialize a calibrated model
calibrated_model = CalibSupport.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# plot the histogram of mean survival time
Fig.graph_histogram(
    observations=calibrated_model.get_all_mean_survival(),
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count')

# report mean and projection interval
print('Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=4))