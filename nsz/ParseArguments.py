from argparse import ArgumentParser

class ParseArguments:
	@staticmethod
	def parse():
		parser = ArgumentParser()
		parser.add_argument('file', nargs='*')
		parser.add_argument('-C', action='store_true', help='Compress NSP/XCI')
		parser.add_argument('-D', action='store_true', help='Decompress NSZ/XCZ/NCZ')
		parser.add_argument('-l', '--level', type=int, default=18, help='Compression Level: Trade-off between compression speed and compression ratio. Default: 18, Max: 22')
		parser.add_argument('-L', '--long', action='store_true', default=False, help='Enables zStandard long distance mode for even better compression')
		parser.add_argument('-B', '--block', action='store_true', default=False, help='Use block compression option. This mode allows highly multi-threaded compression/decompression with random read access allowing compressed games to be played without decompression in the future however this comes with a slightly lower compression ratio cost. This is the default option for XCZ.')
		parser.add_argument('-S', '--solid', action='store_true', default=False, help="Use solid compression option. Slightly higher compression ratio but won't allow for random read access. File compressed this way will never be mountable (have to be installed or decompressed first to run). This is the default option for NSZ.")
		parser.add_argument('-s', '--bs', type=int, default=20, help='Block Size for random read access 2^x while x between 14 and 32. Default: 20 => 1 MB')
		parser.add_argument('-V', '--verify', action='store_true', default=False, help='Verifies files after compression raising an unhandled exception on hash mismatch and verify existing NSP and NSZ files when given as parameter. Requires --keep when used during compression.')
		parser.add_argument('-Q', '--quick-verify', action='store_true', default=False, help='Same as --verify but skips the NSP SHA256 hash verification and only verifies NCA hashes. Does not require --keep when used during compression.')
		parser.add_argument('-K', '--keep', action='store_true', default=False, help='Keep all useless files and partitions during compression to allow bit-identical recreation')
		parser.add_argument('-F', '--fix-padding', action='store_true', default=False, help='Fixes PFS0 padding to match the nxdumptool/no-intro standard. Incompatible with --verify so --quick-verify will be used instead.')
		parser.add_argument('-p', '--parseCnmt', action='store_true', default=False, help='Extract TitleId/Version from Cnmt if this information cannot be obtained from the filename. Required for skipping/overwriting existing files and --rm-old-version to work properly if some not every file is named properly. Supported filenames: *TitleID*[vVersion]*')
		parser.add_argument('-P', '--alwaysParseCnmt', action='store_true', default=False, help='Always extract TitleId/Version from Cnmt and never trust filenames')
		parser.add_argument('-t', '--threads', type=int, default=-1, help='Number of threads to compress with. Numbers < 1 corresponds to the number of logical CPU cores for block compression and 3 for solid compression')
		parser.add_argument('-m', '--multi', type=int, default=4, help='Executes multiple compression tasks in parallel. Take a look at available RAM especially if compression level is over 18.')
		parser.add_argument('-o', '--output', nargs='?', help='Directory to save the output NSZ files')
		parser.add_argument('-w', '--overwrite', action='store_true', default=False, help='Continues even if there already is a file with the same name or title id inside the output directory')
		parser.add_argument('-r', '--rm-old-version', action='store_true', default=False, help='Removes older versions if found')
		parser.add_argument('--rm-source', action='store_true', default=False, help="Deletes source file/s after compressing/decompressing. It's recommended to only use this in combination with --verify")
		parser.add_argument('-i', '--info', action='store_true', default=False, help='Show info about title or file')
		parser.add_argument('--depth', type=int, default=1, help='Max depth for file info and extraction')
		parser.add_argument('-x', '--extract', action='store_true', help='Extract a NSP/XCI/NSZ/XCZ/NSPZ')
		parser.add_argument('--extractregex', type=str, default='', help=r'Regex specifying which files inside the container should be extracted. Example: "^.*\.(cert|tik)$"')
		parser.add_argument('--titlekeys', action='store_true', default=False, help='Extracts titlekeys from your NSP/NSZ files and adds missing keys to ./titlekeys.txt and JSON files inside ./titledb/ (obtainable from https://github.com/blawar/titledb).')
		parser.add_argument('--undupe', action='store_true', help='Deleted all duplicates (games with same ID and Version). The Files folder will get parsed in order so the later in the argument list the more likely the file is to be deleted')
		parser.add_argument('--undupe-dryrun' , action='store_true', help='Shows what files would get deleted using --undupe')
		parser.add_argument('--undupe-rename' , action='store_true', help='Renames files to minimal standard: [TitleId][vVersion].nsz')
		parser.add_argument('--undupe-hardlink' , action='store_true', help='Hardlinks files to minimal standard: [TitleId][vVersion].nsz')
		parser.add_argument('--undupe-prioritylist', type=str, default='', help=r'Regex specifying which dublicate deletion should be prioritized before following the normal deletion order. Example: "^.*\.(nsp|xci)$"')
		parser.add_argument('--undupe-whitelist', type=str, default='', help=r'Regex specifying which dublicates should under no circumstances be deleted. Example: "^.*\.(nsz|xcz)$"')
		parser.add_argument('--undupe-blacklist', type=str, default='', help=r'Regex specifying which files should always be deleted - even if they are not even a dublicate! Be careful! Example: "^.*\.(nsp|xci)$"')
		parser.add_argument('--undupe-old-versions',action='store_true', default=False, help='Removes every old version as long there is a newer one of the same titleID.')
		parser.add_argument('-c', '--create', help='Inverse of --extract. Repacks files/folders to an NSP. Example: --create out.nsp .\\in')
		parser.add_argument('--machine-readable', action='store_true', default=False, help='Restricts terminal output and reports in a way that is easier for a machine to read.')

		args = parser.parse_args()
		return args
