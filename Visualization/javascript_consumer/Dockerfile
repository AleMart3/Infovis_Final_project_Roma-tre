FROM node:10

WORKDIR /usr/src/app

RUN npm install && npm init -y && npm install socket.io@2.2.0 && npm install express@4.17.1 && npm install body-parser@1.19.0 && npm install kafkajs@1.9.3

COPY . .

EXPOSE 3001

ADD ./javascript_server_side.js javascript_server_side.js

CMD ["node", "javascript_server_side.js"]