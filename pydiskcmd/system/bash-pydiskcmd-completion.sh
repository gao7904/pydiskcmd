# bash tab completion for the nvme command line utility

_pysata_cmds="check-PowerMode accessible-MaxAddress identify self-test \
          smart standby read write flush trim version help"

_pynvme_cmds="list smart-log id-ctrl id-ns error-log fw-log fw-download fw-commit \
          version help"

pysata_list_opts () {
    local opts=""
	local compargs=""

	local nonopt_args=0
	for (( i=0; i < ${#words[@]}-1; i++ )); do
		if [[ ${words[i]} != -* ]]; then
			let nonopt_args+=1
		fi
	done

	if [ $nonopt_args -eq 2 ]; then
		opts="/dev/sd* "
	fi

	opts+=" "

    case "$1" in
		"check-PowerMode")
		opts+=" --show_status -h --help"
		;;
        "accessible-MaxAddress")
		opts+=" --show_status -h --help"
		;;
        "identify")
		opts+=" -o --output-format= --show_status -h --help"
		;;
        "self-test")
		opts+=" -t --test= --show_status -h --help"
		;;
        "smart")
		opts+=" --show_status -h --help"
		;;
        "standby")
		opts+=" --show_status -h --help"
		;;
        "read")
		opts+=" -s --start-block= -c --block-count= -b --block-size= \
            --show_status -h --help"
		;;
        "write")
		opts+=" -s --start-block= -c --block-count= -d --data= \
            -f --data-file= -b --block-size= --show_status -h --help"
		;;
        "flush")
		opts+=" --show_status -h --help"
		;;
        "trim")
		opts+=" -r --block_range= --show_status -h --help"
		;;
        "version")
		opts+=""
			;;
		"help")
		opts+=""
			;;
    esac

        opts+=" -h --help"

	COMPREPLY+=( $( compgen $compargs -W "$opts" -- $cur ) )

	return 0
}


pynvme_list_opts () {
        local opts=""
	local compargs=""

	local nonopt_args=0
	for (( i=0; i < ${#words[@]}-1; i++ )); do
		if [[ ${words[i]} != -* ]]; then
			let nonopt_args+=1
		fi
	done

	if [ $nonopt_args -eq 2 ]; then
		opts="/dev/nvme* "
	fi

	opts+=" "

    case "$1" in
        "list")
		opts+=" -o --output-format= -h --help"
		;;
        "smart-log")
		opts+=" -o --output-format= -h --help"
		;;
        "id-ctrl")
		opts+=" -o --output-format= -h --help"
		;;
        "id-ns")
		opts+=" -n --namespace-id= -o --output-format= -h --help"
		;;
        "error-log")
		opts+=" -o --output-format= -h --help"
		;;
        "fw-log")
		opts+=" -o --output-format= -h --help"
		;;
        "fw-download")
		opts+=" -f --fw= -x --xfer= -o --offset= -h --help"
		;;
        "fw-commit")
		opts+=" -s --slot= -a --action= -h --help"
		;;
        "version")
		opts+=""
			;;
		"help")
		opts+=""
			;;
    esac

        opts+=" -h --help"

	COMPREPLY+=( $( compgen $compargs -W "$opts" -- $cur ) )

	return 0
}


_pysata_subcmds () {
        local cur prev words cword
	_init_completion || return

	if [[ ${#words[*]} -lt 3 ]]; then
		COMPREPLY+=( $(compgen -W "$_pysata_cmds" -- $cur ) )
	else
		pysata_list_opts ${words[1]} $prev
	fi

	return 0
}

_pynvme_subcmds () {
        local cur prev words cword
	_init_completion || return

	if [[ ${#words[*]} -lt 3 ]]; then
		COMPREPLY+=( $(compgen -W "$_pynvme_cmds" -- $cur ) )
	else
		pynvme_list_opts ${words[1]} $prev
	fi

	return 0
}

complete -o default -F _pysata_subcmds pysata

complete -o default -F _pynvme_subcmds pynvme
