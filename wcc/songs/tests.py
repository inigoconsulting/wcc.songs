
        # Integration tests for Song
        ztc.ZopeDocFileSuite(
            'Song.txt',
            package='wcc.songs',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

