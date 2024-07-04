import method_position_independent as mpi
import method_position_dependent as mpd
import method_pre_process as mpp


def seg_method_choose(text):
    if text == 'origin':
        return mpi.origin, True
    elif text == 'kmeans':
        return mpi.kmeans_3d, True
    elif text == 'gmm':
        return mpi.gmm_3d, True
    elif text == 'otsu':
        return mpi.otsu_3d, True
    elif text == 'kapur_entropy':
        return mpi.kapur_entropy_3d, True
    elif text == 'watershed':
        return mpd.watershed, False


def pre_method_choose(text):
    if text == 'origin':
        return mpp.origin
    elif text == 'gamma':
        return mpp.adjust_gamma
    elif text == 'equalized':
        return mpp.equalized_hist
    elif text == 'median':
        return mpp.median
