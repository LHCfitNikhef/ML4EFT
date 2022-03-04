import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


def read_param_value(wc = 'chdd'):
    '''
    Function to read parameter value from param card
    '''
    filename = 'lin/'+wc+'/param_card.dat'
    match_number = re.compile('[-+]?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?')
    with open(filename,'r') as f:
        data = f.readlines()
        f.close()
    for line,next_line in zip(data, data[1:]+[data[0]]):
        if 'Block smeft' in line:
            final_list = [float(x) for x in re.findall(match_number, next_line)]
            param = float(final_list[-1])
            break
    return param

def predictions(coefficients, bins, nreps=50):
    nbins = np.size(bins)-1

    predictions = dict()


    #SM predictions
    SMpredictions = np.zeros(nreps*nbins).reshape(nreps, nbins)
    for mcrep in np.arange(nreps):
        df = pd.read_pickle('sm/events_'+str(mcrep)+'.pkl.gz')
		
        sigma = df['pt_z'][0]
        nevents = np.size(df['pt_z'])-1

        n,bins,patches = plt.hist(x = df['pt_z'][1:], bins=bins);
        SMpredictions[mcrep,:] = n*sigma/nevents
    
    predictions['sm'] = np.average(SMpredictions, axis=0)


	#SMEFT predictions
    for coeff in coefficients:
        EFTpredictions = np.zeros(nreps*nbins).reshape(nreps, nbins)
        for mcrep in np.arange(nreps):
            #Read dataframe and WC value
            df = pd.read_pickle('lin/'+coeff+'/events_'+str(mcrep)+'.pkl.gz')
            wc = read_param_value(coeff)

            #Get total cross section and number of generated events
            sigma = df['pt_z'][0]
            nevents = np.size(df['pt_z'])-1

            n, bins, patches = plt.hist(x = df['pt_z'][1:], bins=bins)
            sigma_EFT = n*sigma/nevents

            sigma_1 = (1./wc)*(sigma_EFT - predictions['sm'])
            EFTpredictions[mcrep,:] = sigma_1
			
        predictions[coeff] = np.average(EFTpredictions, axis=0)

    bin_index = ['Bin '+str(s+1) for s in np.arange(nbins)]
    df = pd.DataFrame(predictions, index=bin_index).T
    #df.set_index('Bins',inplace=True)
	
    df.to_pickle("./zh_th_predictions.pkl")  	



if __name__=='__main__':
    coeffs = ['chdd', 'chwb', 'cbhre', 'chw']
    bins = np.array([0, 75, 150, 250, 400, 1000])
    #bins = np.array([0, 10000])
    predictions(coeffs, bins)
