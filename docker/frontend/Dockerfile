FROM node:16-buster-slim

WORKDIR /usr/app/

COPY /../../frontend/package.json /

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]