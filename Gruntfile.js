module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      options: {
        separator: '\n;\n'
      },
      all: {
        files: {
          'us_ignite/static/js/script.js': [
            'us_ignite/static/js/source/libs.js',
            'us_ignite/static/js/source/app.js',
            'us_ignite/static/js/source/script.js'
          ]
        }
      }
    },

    uglify: {
      options: {
        mangle: {
          except: []
        }
      },
      all: {
        files: {
          'us_ignite/static/js/script.min.js': 'us_ignite/static/js/script.js'
        }
      }
    },

    sass: {
      options: {
        sourceComments: true
      },
      dist: {
        options: {
          outputStyle: 'uncompressed',
          sourceComments: true
        },
        files: {
          'us_ignite/static/css/style.css': 'us_ignite/static/scss/app.scss',
        }
      }
    },

    

    watch: {
      grunt: { files: ['Gruntfile.js'] },

      sass: {
        files: 'us_ignite/static/scss/**/*.scss',
        tasks: ['sass']
      },
      js: {
        files: 'us_ignite/static/js/**/*.js',
        tasks: ['buildjs']
      }
    }
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.registerTask('build', ['sass']);
  grunt.registerTask('buildjs', ['concat', 'uglify']);
  grunt.registerTask('default', ['build','buildjs', 'watch']);
}
