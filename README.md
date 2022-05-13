# csc3170
Including nature language processing sentiment-analysis and Rate my prof. website and database design

# Database ER diagram:

![image](https://user-images.githubusercontent.com/88835096/168282548-fd0b0b17-dcd3-473b-a345-66782e90d380.png)

#Hashing
Using hashing method to encode the password, and save it in the database. This action will increase the security of the database:
-- 
- The origin password is 123456, after hashing, it was encode to a 48 byte hashing code:
- ![Screenshot from 2022-05-13 17-10-26](https://user-images.githubusercontent.com/88835096/168283160-146a55e3-6303-4367-9d64-e6fc8ce6fb7d.png)
- ![Screenshot from 2022-05-13 17-09-30](https://user-images.githubusercontent.com/88835096/168283200-75d63b88-5338-4a77-854e-b939b7468354.png)

# using the hidden_tag function to increase the security of the website:
when some hackers need to steal the info from your submit page, they will use the Cross Site Request Forgery(CSRF)
using hidden_tag() function:
detailed information is in: https://dl.acm.org/doi/abs/10.1145/1455770.1455782 (Robust defenses for cross-site request forgery.  Authors: Adam Barth, Collin Jackson, John C. Mitchell)
