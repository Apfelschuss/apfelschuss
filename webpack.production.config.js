const path = require('path')
const glob = require('glob')
const autoprefixer = require('autoprefixer');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const webpack = require('webpack')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')
const PurgecssPlugin = require('purgecss-webpack-plugin')

const configs = [{
  mode: 'production',
  entry: './apfelschuss/src/index.js',
  output: {
    path: path.resolve(__dirname, './apfelschuss/static'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        use: 'babel-loader',
      },
      {
        test: /\.(sass|scss)$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
                plugins: () => [autoprefixer()]
            }
          },
          'sass-loader'
        ]
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader'
        ]
      },
      {
        test: /\.(gif|png|jpe?g|svg)$/i,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192,
              name: '[name].[ext]',
              fallback: 'file-loader',
              outputPath: 'img',
            },
          },
          {
            loader: 'image-webpack-loader',
            options: {
              mozjpeg: {
                mozjpeg: {
                  progressive: true,
                  quality: 65,
                },
                pngquant: {
                  quality: '65-90',
                  speed: 4,
                },
                gifsicle: {
                  interlaced: false,
                },
                webp: {
                  quality: 75,
                },
              },
            },
          },
        ],
      },
      {
        resolve: {
          extensions: ['.js'],
          alias: {
            'jquery': 'jquery/dist/jquery.slim.js',
          }
        },
      }
    ],
  },

  plugins: [
    new CleanWebpackPlugin({
      cleanOnceBeforeBuildPatterns: ['**/*', '!.gitkeep'],
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      Popper: ['popper.js', 'default']
    }),
    new CopyWebpackPlugin([
      {
        from: './apfelschuss/src/public',
        to: 'public',
      },
    ]),
    new UglifyJsPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].css',
    }),
    new PurgecssPlugin({
        paths: glob.sync('./apfelschuss/templates/**/*.html', { nodir: true }),
        whitelist: ['show']
    })
  ]
}
]

module.exports = configs
