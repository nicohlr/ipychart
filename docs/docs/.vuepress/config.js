module.exports = ctx => ({

    title: 'ipychart',
    description: 'A Jupyter - Chart.js bridge enabling interactive data visualization in the Jupyter notebook.',
    //base: '/<REPO>/', 
    head: [
        ['link', { rel: 'icon', href: '/favicon.ico' }]
    ],

    themeConfig: {

        repo: 'https://github.com/nicohlr/ipychart',
        editLinks: false,
        docsDir: 'docs',
        logo: '/ipychart-logo.svg',

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
                link: '/developer_guide/development_installation',
            },
        ],
        sidebarDepth: 5,
        sidebar: [
            {
                title: 'User Guide',
                collapsable: false,
                sidebarDepth: 1,
                children: ['/user_guide/introduction', '/user_guide/getting_started', '/user_guide/usage', '/user_guide/charts', '/user_guide/config', '/user_guide/advanced'],
            },
            {
                title: 'Developer Guide',
                collapsable: false,
                sidebarDepth: 0,
                children: [
                    '/developer_guide/development_installation',
                    '/developer_guide/documentation',
                    '/developer_guide/publish',
                ],
            },
        ],
    }
})
