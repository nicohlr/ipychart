module.exports = ctx => ({

    title: 'ipychart',
    description: 'A Jupyter - Chart.js bridge enabling interactive data visualization in the Jupyter notebook.',
    //base: '/<REPO>/', 
    head: [
        ['link', {rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png'}],
        ['link', {rel: 'icon', type:'image/png', sizes: '192x192', href: '/android-chrome-192x192.png'}],
        ['link', {rel: 'icon', type:'image/png', sizes: '32x32', href: '/favicon-32x32.png'}],
        ['link', {rel: 'icon', type:'image/png', sizes: '16x16', href: '/favicon-16x16.png'}],
        ['link', {rel: 'manifest', href: '/site.webmanifest'}],
        ['link', {rel: 'mask-icon', href: '/safari-pinned-tab.svg', color:"#36a3ec"}],
        ['meta', {name: 'msapplication-TileImage', content: '/mstile-150x150.png'}],
        ['meta', {name: 'msapplication-TileColor', content: '#2b5797'}],
        ['meta', {name: 'theme-color', content: '#ffffff'}],
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
                children: [
                    '/user_guide/introduction', 
                    '/user_guide/getting_started', 
                    '/user_guide/usage', 
                    '/user_guide/charts', 
                    '/user_guide/config', 
                    '/user_guide/scales', 
                    '/user_guide/advanced'
                ],
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
