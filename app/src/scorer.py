import pandas as pd
import joblib
import lightgbm as lgb

# Make prediction
def make_pred(dt, path_to_file):

    print('Importing pretrained model...')
    # Import model
    model = joblib.load('./models/model.joblib')

    predictions = model.predict(dt)

    # Make submission dataframe
    submission = pd.DataFrame({'client_id': pd.read_csv(path_to_file)['client_id'], 'preds': predictions})
    # submission = pd.DataFrame({
    #     'client_id':  pd.read_csv(path_to_file)['client_id'],
    #     'preds': (model.predict_proba(dt)[:, 1] > model_th) * 1
    # })
    print('Prediction complete!')

    # Return proba for positive class
    return submission