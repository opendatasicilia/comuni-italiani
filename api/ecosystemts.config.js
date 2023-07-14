module.exports = {
  apps: [
    {
      name: "api.infocomuni.eu",
      script: "node",
      watch: true,
      args: "index.js",
      env: {
        NODE_ENV: "production",
      },
      exp_backoff_restart_delay: 100,
    },
  ],
};
