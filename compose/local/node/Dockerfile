FROM node:10-stretch-slim

WORKDIR /app
COPY ./package.json /app
RUN npm install && npm cache clean --force
COPY . /app
RUN npm run build

ENV PATH ./node_modules/.bin/:$PATH
