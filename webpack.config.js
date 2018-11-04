const Encore = require('@symfony/webpack-encore')
const BrowserSyncPlugin = require('browser-sync-webpack-plugin')
const dotEnvSafe = require('dotenv-safe')
const path = require('path')
const { writeCompiledConfig } = require('./utils/encore')
const config = {
	outputDir: 'static/build',
}
module.exports.config = config
dotEnvSafe.load({
	path: path.resolve(process.cwd(), Encore.isProduction()
		? '.env-dev.example'
		: '.env-dev',
	),
	sample: path.resolve(process.cwd(), '.env-dev.example'),
	allowEmptyValues: true,
})
const env = {
	BROWSERSYNC_PORT: Number(process.env.BROWSERSYNC_PORT),
	BROWSERSYNC_OPEN: JSON.parse(process.env.BROWSERSYNC_OPEN),
	BROWSERSYNC_PROXY: String(process.env.BROWSERSYNC_PROXY),
}
Encore
	.setOutputPath(config.outputDir)
	.setPublicPath('/static/build')
	.cleanupOutputBeforeBuild([
		'**/*.js',
		'**/*.css',
		'**/*.map',
		'manifest.json',
	])
	.enableBuildNotifications()
	.enableSourceMaps(!Encore.isProduction())
	.enableVersioning(Encore.isProduction())
	.configureUglifyJsPlugin(options => {
		if (Encore.isProduction()) {
			options.compress = {
				warnings: false,
				drop_console: true,
			}
			options.comments = false
		}
	})
	.addEntry('script', `./resources/script.js`)
	.createSharedEntry('vendor', [
		'vue/dist/vue',
		`./resources/utils/polyfills.js`,
	])
	.addStyleEntry('style', `./resources/style.scss`)
	.enablePostCssLoader()
	.enableSassLoader()
	.enableVueLoader()
const webpackConfig = Encore.getWebpackConfig()
if (!Encore.isProduction()) {
	addBrowserSyncPlugin()
}
addAliases()
configureModuleRules()
if (!Encore.isProduction()) {
	// Set compiled config in Intellij preferences
	writeCompiledConfig(webpackConfig)
}
function addAliases() {
	webpackConfig.resolve.alias = {
		// Use minified version of Vue on production
		'vue/dist/vue': Encore.isProduction()
			? 'vue/dist/vue.min'
			: 'vue/dist/vue',
	}
}
function configureModuleRules() {
	for (let rule of webpackConfig.module.rules) {
		if (rule.use) {
			for (let loader of rule.use) {
				if (loader.loader === 'babel-loader') {
					// By default, Babel excludes modules imported from node_modules
					// But UglifyJS still does not supports ES6 syntax
					// So, please, do not exclude node_modules from Babel
					// https://github.com/symfony/webpack-encore/issues/139#issuecomment-322592989
					delete rule.exclude
				}
			}
		}
	}
}
function addBrowserSyncPlugin() {
	webpackConfig.plugins.push(new BrowserSyncPlugin({
		port: env.BROWSERSYNC_PORT,
		proxy: env.BROWSERSYNC_PROXY,
		open: env.BROWSERSYNC_OPEN,
		// does not work with html-webpack-plugin
		reloadOnRestart: true,
		files: [
			path.join(config.outputDir, '*.css'),
			path.join(config.outputDir, '*.js'),
			'**/*.pug',
		],
	}, {
		reload: false,
		name: 'bs-webpack-plugin',
	}))
}
module.exports = webpackConfig
