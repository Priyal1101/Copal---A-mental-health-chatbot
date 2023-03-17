# Copal- A Mental Health Chatbot ![image](https://user-images.githubusercontent.com/91384754/225904068-5b4b8da7-d315-467f-b1bb-e6fae9f13ba9.png)


![Issues](https://img.shields.io/github/issues/Priyal1101/Copal---A-mental-health-chatbot)
![Pull Requests](https://img.shields.io/github/issues-pr/Priyal1101/Copal---A-mental-health-chatbot)
![Forks](https://img.shields.io/github/forks/Priyal1101/Copal---A-mental-health-chatbot)
![Stars](https://img.shields.io/github/stars/Priyal1101/Copal---A-mental-health-chatbot)
[![License](https://img.shields.io/github/license/aresgodd/Diabeto)](https://github.com/Priyal1101/Copal---A-mental-health-chatbot)


Mental health is a vital part of our society, and the need for accessible mental health resources has never been greater. Copal, a mental health chatbot created using Intel One API, provides a safe, non-judgmental space for individuals to seek help and access mental health resources. By using advanced algorithms, deep learning models, and optimized performance and parallelized computation, Copal aims to bridge the gap between those in need and the resources available to them. This chatbot is an effort to help individuals dealing with mental health issues and substance use disorders, which affect more than 13% of the world's population, according to a research performed by the World Health Organization (WHO).

# Importance ![image](https://user-images.githubusercontent.com/91384754/225901359-22287e48-ffc3-4d11-baed-ab72a29f46d6.png)

In 2019, it was estimated that around 970 million people around the world were living with a mental disorder, with anxiety and depressive disorders being the most common. However, despite the availability of effective prevention and treatment options, most people with mental disorders do not have access to effective care. In addition, many people also experience stigma, discrimination, and violations of human rights, making it even harder for them to seek help.

The COVID-19 pandemic has further highlighted the need for accessible mental health resources. According to initial estimates, in just one year, there has been a 26% increase in anxiety disorders and a 28% increase in major depressive disorders. Copal's aim is to bridge the gap between those who need mental health resources and the resources available to them, providing a platform for people to seek help in a safe, non-judgmental environment.

# What Inspired US ![image](https://user-images.githubusercontent.com/91384754/225822955-0a1dbf6a-bc75-4daf-95c7-779d1722f4db.png)

The need for a mental health chatbot that can assist users with their mental health concerns. This chatbot aims to provide a safe and anonymous space for users to discuss their symptoms, thoughts, behaviors, and techniques to manage their mental health.


# What It Does ![image](https://user-images.githubusercontent.com/91384754/225822847-aa3d4c67-91db-447d-9c64-b992baef8fe9.png)

The chatbot talks to people about what they might be feeling and tries to provide them with a base analysis of their conditions and tries to provide them solutions that they can follow to be able to deal with their symptoms and seek professional help when they can.

# How Is It Built ![image](https://user-images.githubusercontent.com/91384754/225824434-0688fac8-2e5f-4f23-b8d1-2576d5b64788.png)

### 📚 Libraries
The first step was to import the necessary libraries. I used Python and some popular libraries for natural language processing, such as nltk and sklearn.

### 🖥 User Input
Next, I created a user input system where the user can enter their message or question. The chatbot then processes the input and generates an appropriate response.

### 🔤 Keywords and Responses
I defined a set of keywords and their corresponding responses. This helps the chatbot to understand the user's intent and generate an appropriate response.

### 🧠 Functions
I defined several functions that can help the chatbot to understand the user's input. These functions include techniques for tokenizing, stemming, and lemmatizing the input text.

### 🗣 Generating Responses
Using the keywords and functions mentioned above, the chatbot generates an appropriate response to the user's input.

### 💾 Saving the Model and Integrating with Frontend
Finally, I saved the model and integrated it with a simple frontend application. This allows users to interact with the chatbot and get responses in real-time.

# What We learned ![image](https://user-images.githubusercontent.com/91384754/225822729-c2c94061-3378-4723-ad64-bd4fef41c6ae.png)

### 🚀 Building the Chatbot
The first step was to build the chatbot itself. I used Python and a variety of libraries to create a chatbot that can communicate with users and collect information about their mental health.

### 🤔 Emotional Science
During the development process, I gained a deeper understanding of the various emotions that people might feel on a daily basis and how they can potentially lead to more serious mental health issues if left unaddressed. I incorporated this knowledge into the chatbot's design to help users more effectively communicate their emotional state.

### 🤖 Machine Learning
I also learned about different machine learning algorithms and how they can be applied to predict user responses and make recommendations for improvement. This allowed the chatbot to provide personalized support and advice to each user based on their individual needs.

### 📊 Data Analysis
To build an effective chatbot, I had to collect and analyze large amounts of data, including user emotions. This helped me to understand the most common mental health issues that people face and how best to address them through the chatbot.

These are just a few examples of the knowledge and skills that i likely gained while building this project. 
Overall, building a mental health chatbot is a challenging and rewarding experience that requires a combination of technical expertise and psychological knowledge.

# Use of Intel OneAPI ![image](https://user-images.githubusercontent.com/91384754/225903825-99247013-9192-4eea-a637-7c448efb92b3.png)


![image](https://user-images.githubusercontent.com/91384754/225832421-df1060a4-f0d0-4ff8-a83f-660a7e2e0175.png)

## Libraries Used ![image](https://user-images.githubusercontent.com/91384754/225903929-286f9d00-d61e-4c53-87f9-9c3f4f2947a4.png)

### SYCL/DPC++ 🚀
The SYCL/DPC++ library is used to optimize performance and parallelize computation in the chatbot. This library allows the code to be written in a high-level language, while still being able to take advantage of heterogeneous computing resources such as GPUs, CPUs, and FPGAs. By using SYCL/DPC++, the chatbot can achieve faster response times and more accurate results.

### oneMKL 🔢
The oneMKL library provides highly optimized math functions, which are useful in implementing algorithms that involve computations such as matrix multiplication and convolution. These computations are often used in natural language processing tasks, such as language translation and sentiment analysis. By using oneMKL, the chatbot can achieve faster and more efficient computations.

### oneDNN 🧠
The oneDNN library provides highly optimized deep learning primitives, which is useful in implementing deep learning models for the chatbot. These primitives include convolution, pooling, and normalization, which are essential in building and training neural networks. By using oneDNN, the chatbot can achieve better accuracy and faster training times.

### oneTBB ⚡️
The oneTBB library provides a task-based parallelism framework, which is used to parallelize computations in the chatbot. This framework allows the chatbot to efficiently use system resources by distributing tasks across multiple threads. By using oneTBB, the chatbot can achieve faster response times and more efficient use of system resources.

### oneDAL 📊
The oneDAL library provides highly optimized data analytics primitives, which could be useful in implementing algorithms for data preprocessing and analysis in the chatbot. These primitives include data compression, random number generation, and sorting. By using oneDAL, the chatbot can achieve faster and more efficient data processing.

### Conclusion 🎉
In summary, these libraries are used to optimize performance and parallelize computation in a chatbot. By using these libraries, the chatbot can achieve faster response times, better accuracy, and more efficient use of system resources.

## Implementation ![image](https://user-images.githubusercontent.com/91384754/225903405-16d88e58-1c42-4d61-9551-3627916c1622.png)

![image](https://user-images.githubusercontent.com/91384754/225829797-f736c6bf-0301-4512-8cdf-deeb3f3b1a3a.png)

# Final Result ![image](https://user-images.githubusercontent.com/91384754/225901915-e9cbf366-4275-4949-9e50-0fb180da9738.png)

![image](https://user-images.githubusercontent.com/91384754/225825988-9dc194e6-cb0b-4916-b877-57ecf49305fb.png)


# Tools Used ![image](https://user-images.githubusercontent.com/91384754/225901965-629c052a-5394-4631-a7ad-ac7fb9797c0a.png)

![image](https://user-images.githubusercontent.com/91384754/225823220-6bf01148-0591-46ee-9204-9fac15a82028.png)
![image](https://user-images.githubusercontent.com/91384754/225823265-3a47c27e-c89e-4dac-b5cf-930a57789602.png)
![image](https://user-images.githubusercontent.com/91384754/225823281-aa1c4aa7-f8ea-42a9-8c10-3adc60b5cc57.png)
![image](https://user-images.githubusercontent.com/91384754/225823348-6900e4fd-7054-4d11-baae-ca0111d2ce13.png)

# Contributors ![image](https://user-images.githubusercontent.com/91384754/225902068-ccb9f7ff-2f90-4f49-b307-0695951f03a8.png)

[Navya Dua](https://github.com/navyadua)

[Priyal Jhunjhunwala](https://github.com/Priyal1101)

[Samyak Jain](https://github.com/samyakjain1010)

[Pratham Patel](https://github.com/Prathampatel12)

# 

Thank You for checking out our project!😉 We believe in creating a better world through technology⚙️, and we hope this project contributes to that goal.👍🏻

# 


