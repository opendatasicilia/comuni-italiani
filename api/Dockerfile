FROM node:20
WORKDIR /app/api
COPY package.json ./
RUN test -f yarn.lock && cp yarn.lock . || echo "No yarn.lock found"
RUN yarn install
COPY . .
EXPOSE 8888
