module.exports = {
    env: {
        browser: true,
        es2021: true,
    },
    extends: ['airbnb-base'],
    parserOptions: {
        ecmaVersion: 13,
        sourceType: 'module',
    },
    rules: {
        indent: ['error', 4],
        'no-console': 'off',
        'no-param-reassign': 'off',
    },
};
