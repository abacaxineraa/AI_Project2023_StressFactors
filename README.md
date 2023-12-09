# AI_Project2023

Marina Flat, Ana Torres, Jeong Yeon Nam
Project Summary
The level of student stress is an important issue in the educational field today. Depending on many factors that affect a student's stress level, the educational process can be either successful or not. The goal of our project was to predict the stress level of a student depending on various factors. As a target audience we assume students, particularly the ones with high anxiety levels, would benefit from this AI. School counsellors would too, as it would help them offer help to the ones that need it.

We obtained our data from a dataset available on Kaggle, an online community of data scientists and machine learning practitioners under Google LLC. The dataset contains around 20 features that create the most impact on the anxiety of a student. The features were selected scientifically considering one of the major factors provided in the dataset:

Data Attributes:  Psychological Factors => 'anxiety_level', 'self_esteem', 'mental_health_history', 'depression', Physiological Factors => 'headache', 'blood_pressure', 'sleep_quality', 'breathing_problem Environmental Factors => 'noise_level', 'living_conditions', 'safety', 'basic_needs', Academic Factors => 'academic_performance', 'study_load', 'teacher_student_relationship', 'future_career_concerns', Social Factor => 'social_support', 'peer_pressure', 'extracurricular_activities', 'bullying'

The next step was to check how clean the database was. For this purpose, we employed certain methods and concluded that the selected database is sufficiently clean and can be further used for building the model.

We chose to use Linear regression is a classic and widely used model for predicting a continuous variable, making it a suitable choice for your regression task. It assumes a linear relationship between the input features and the target variable, making it interpretable and easy to implement. Linear regression is chosen for its simplicity, interpretability, and ease of implementation. In the context of predicting anxiety levels based on a variety of factors, it allows us to establish a clear linear relationship between these factors.

The training process involved fitting the linear regression model to the prepared training data, which includes the features and the target variable (anxiety level). The model learns the weights that minimize the difference between the predicted anxiety levels and the actual values in the training set.

During the work on the model, we referred to the Open AI’s ChatGPT to clarify some details of the code and other questions. As a result, we visualized our model and were able to clearly see which factors have the greatest impact on student stress.

Throughout this project, our team gained a deeper understanding of regression tasks in the context of AI. We learned how to use linear regression as a suitable model for predicting continuous variables, such as student stress levels, and how to interpret the results.
