FROM node:16-buster-slim

WORKDIR /usr/src/app

COPY /../../frontend/package.json /

RUN npm install

CMD ["npm", "start"]