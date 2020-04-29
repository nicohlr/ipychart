module.exports = ctx => ({

    title: 'ipychart',
    description: 'A Jupyter / Chart.js bridge enabling interactive data visualization in the Jupyter notebook.',
    //base: '/<REPO>/', 
    head: [
        ['link', { rel: 'icon', href: '/favicon.ico' }]
    ],

    themeConfig: {

        repo: 'https://github.com/nicohlr/ipychart',
        editLinks: false,
        docsDir: 'docs',
        logo: '/favicon.ico',

        algolia: ctx.isProd ? ({
            apiKey: '',
            indexName: ''
        }) : null,

        smoothScroll: true,
        nav: [
            {
                text: 'User Guide',
                link: '/user_guide/introduction',
            },
            {
                text: 'Developer Guide',
                link: '/dev_guide/dev_install',
            },
        ],
        sidebarDepth: 5,
        sidebar: [
            {
                title: 'User Guide',
                collapsable: false,
                children: ['/user_guide/introduction', '/user_guide/getting_started', '/user_guide/charts', '/user_guide/config', '/user_guide/advanced'],
            },
            {
                title: 'Developer Guide',
                collapsable: false,
                children: [
                    '/dev_guide/dev_install',
                    '/dev_guide/doc',
                    '/dev_guide/deploy',
                ],
            },
        ],
    }
})
