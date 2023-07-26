

# Next_Word_Recommendation

This project focuses on building a Next Word Recommendation system using Natural Language Processing techniques. The goal is to predict the upcoming words in a given text using LSTM (Long Short-Term Memory) neural networks. The training data for the model is a text document obtained from Google.

## Project Overview

The project primarily involves the following steps:

1. Data Preparation: A text document from Google is used to train the LSTM model. The data is preprocessed to prepare it for training.

2. Model Training: The LSTM and dense Embedded neural networks are implemented for training the Next Word Recommendation system. The training process is time-consuming due to the complexity of the LSTM model.

3. Next Sentence Prediction: A new function is created to predict the next upcoming sentence based on the trained model.

4. Model Persistence: The trained prediction model and tokenizer model are saved using libraries like Pickle and JobLib.

## Project Structure

The project consists of the following files and directories:

- `data/`: Contains the training data and other relevant datasets (if any).

- `notebooks/`: Jupyter notebooks are stored here, showcasing the step-by-step process of the project. The notebooks cover data preprocessing, model training, and evaluation.

- `models/`: This directory contains the saved prediction model and tokenizer model.

- `Nex_Word_prediction.ipynb`: Python script with the main code for training the LSTM model and generating next word recommendations.



## Usage

To use the Next Word Recommendation system, follow these steps:

1. Clone the repository to your local machine.

2. Run the `Nex_Word_prediction.ipynb` script to train the LSTM model.

3. Once the model is trained, you can use the provided function to get predictions for upcoming words in a given text.

## Project Author

This project was developed by Muhammed Thahseer CK, a self-taught data scientist passionate about exploring the field of data science.

## Acknowledgments

Special thanks to the data science community for their valuable resources and tutorials that contributed to the success of this project.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Conclusion

Enjoy exploring the fascinating world of data science through this Next Word Recommendation project. Feel free to go through the notebooks and gain insights into the concepts used in the development process.

Happy learning and data science exploration!
