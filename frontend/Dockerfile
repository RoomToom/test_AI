FROM docker.io/node:23-alpine3.20 AS build
COPY ./package.json ./package-lock.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci
COPY ./ ./
RUN npm run build
FROM docker.io/nginx:latest
COPY --from=build /dist /usr/share/nginx/html
COPY ./src/assets/favicon.ico /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
