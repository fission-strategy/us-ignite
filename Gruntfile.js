module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    concat: {
      options: {
        separator: '\n;\n'
      },
      all: {
        files: {
          'assets/js/script.js': [
            'assets/js/source/libs.js',
            'bower_components/jquery-query-object/jquery.query-object.js',
            'assets/js/source/app.js',
            'assets/js/source/script.js'
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
          'assets/js/script.min.js': 'assets/js/script.js'
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
          'assets/css/style.css': 'assets/scss/app.scss',
        }
      }
    },

    

    watch: {
      grunt: { files: ['Gruntfile.js'] },

      sass: {
        files: 'assets/scss/**/*.scss',
        tasks: ['sass']
      },
      js: {
        files: 'assets/js/**/*.js',
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
