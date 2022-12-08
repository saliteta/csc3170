# CSC3170 Course Project
This repository includes the **Nature Language Processing Sentiment-Analysis** part and the **Rate My Professor** website, including the database design.

# Database ER diagram:

![image](https://user-images.githubusercontent.com/88835096/168282548-fd0b0b17-dcd3-473b-a345-66782e90d380.png)

#Hashing
Using hashing method to encode the password, and save it in the database. This job will increase the security of the database:
- The origin password is 123456, after hashing, it was encode to a 48 byte hashing code:
- ![Screenshot from 2022-05-13 17-10-26](https://user-images.githubusercontent.com/88835096/168283160-146a55e3-6303-4367-9d64-e6fc8ce6fb7d.png)
- ![Screenshot from 2022-05-13 17-09-30](https://user-images.githubusercontent.com/88835096/168283200-75d63b88-5338-4a77-854e-b939b7468354.png)

# Further Security Ensurance
Using the `hidden_tag` function to increase the security of the website: when some hackers need to steal the info from your submit page, they will need to pass the Cross Site Request Forgery(CSRF) using `hidden_tag()`.
- The detailed information is in [https://dl.acm.org/doi/abs/10.1145/1455770.1455782](https://dl.acm.org/doi/abs/10.1145/1455770.1455782), i.e. Robust defenses for cross-site request forgery.
- Authors of this paper : Adam Barth, Collin Jackson, John C. Mitchell)


# Data analysis:
- Using the NLP technique to do the sentiment analysis
- Using the LSTM and BERT network. training dataset: twitter. Test dataset: Jobs' talk in Standford
- Detailed information of LSTM(A. Graves, N. Jaitly and A. Mohamed, "Hybrid speech recognition with Deep Bidirectional LSTM," 2013 IEEE Workshop on Automatic Speech Recognition and Understanding, 2013, pp. 273-278, doi: 10.1109/ASRU.2013.6707742)
- Detailed Information of BERT(BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. Author: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. arXiv:1810.04805)
![image](https://user-images.githubusercontent.com/88835096/168285978-1ff61eb0-22bf-453d-8441-a845ec56edb5.png)
