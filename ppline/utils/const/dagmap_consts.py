DAG_NAME_KEYNAME = 'PIPELINE_NAME'
PROJECT_DIR = ''

PROJECT_DIR_KEYNAME = 'PROJECT_DIR'

# STEPS INSTRUCTIONS
STEPS_KEYNAME = 'steps'
DEPENDS_ON_KEYNAME = 'depends_on'
EXEC_KEYNAME = 'exec'
EXEC_PATH_SEPARATOR = ':'

# PARAMS_KEYNAME = 'context'
# GENERATE_WITH_KEYNAME = 'generate_with'

# INDEXED_INPUTS_KEYNAME = 'inputs'
# NAMED_INPUTS_KEYNAME = 'named_inputs'
# ALL_INPUTS_KEYNAME = '*'



























# # SETUP INSTRUCTIONS

# SETUP_KEYNAME = 'setup'


# DAGESTATOR_SETUP_KEYNAME = 'dagestator'

# DAGESTATOR_STRICT_MODE_KEYNAME = 'STRICT_MODE'
# DAGESTATOR_STRICT_MODE_DEFAULT = False

# DISABLE_LOW_EVENTS_KEYNAME = 'ENABLE_LOW_EVENTS'
# DISABLE_LOW_EVENTS_DEFAULT = False

# DAGESTATOR_LOG_DIR_KEYNAME = 'LOG_DIR'
# DAGESTATOR_LOG_DIR_DEFAULT = None

# DAGESTATOR_LOG_FILENAME_KEYNAME = 'LOG_FILENAME'
# DAGESTATOR_LOG_FILENAME_DEFAULT = None

# DAGESTATOR_LOG_LEVEL_KEYNAME = 'LOG_LEVEL'
# DAGESTATOR_LOG_LEVEL_DEFAULT = 'INFO'


# RUNNER_SETUP_KEYNAME = 'runner'

# PROJECT_NAME_KEYNAME = 'PROJECT_NAME'

# ENABLE_MP_KEYNAME = 'ENABLE_MP'
# ENABLE_MP_DEFAULT = False

# ITER_SLEEP_SEC_KEYNAME = 'ITER_SLEEP_SEC'
# ITER_SLEEP_SEC_DEFAULT = 1

# FREE_CPU_COUNT_KEYNAME = 'FREE_CPU_COUNT'
# FREE_CPU_COUNT_DEFAULT = 1

# RUNNER_STRICT_MODE_KEYNAME = 'STRICT_MODE'
# RUNNER_STRICT_MODE_DEFAULT = False

# DAG_NAME_KEYNAME = 'PIPELINE_NAME'
# DAG_NAME_DEFAULT = 'dag'

# DAG_CONFIG_KEYNAME = 'DAG_CONFIG'
# DAG_CONFIG_DIR_KEYNAME = 'DAG_CONFIG_DIR'

# RUNNER_LOG_DIR_KEYNAME = 'LOG_DIR'
# RUNNER_LOG_DIR_DEFAULT = 'wombat_log'

# RUNNER_LOG_FILENAME_KEYNAME = 'LOG_FILENAME'
# RUNNER_LOG_FILENAME_DEFAULT = 'runner.log'

# RUNNER_LOG_LEVEL_KEYNAME = 'LOG_LEVEL'
# RUNNER_LOG_LEVEL_DEFAULT = 'INFO'

# LOCAL_STORAGE_DIR_KEYNAME = 'LOCAL_STORAGE_DIR'
# LOCAL_STORAGE_DIR_DEFAULT = 'wombat_storage'

# MAX_DISK_SPACE_USAGE_BYTES_KEYNAME = 'MAX_DISK_SPACE_USAGE_BYTES'
# MAX_DISK_SPACE_USAGE_PERCENT_KEYNAME = 'MAX_DISK_SPACE_USAGE_PERCENT'

# UPLOAD_CHUNK_BYTES_KEYNAME = 'UPLOAD_CHUNK_BYTES'
# UPLOAD_CHUNK_BYTES_DEFAULT = 100 * 1024 * 1024  # 100 MB

# HASH_CHUNK_BYTES_KEYNAME = 'HASH_CHUNK_BYTES'

# SENTRY_DNS_KEYNAME = 'SENTRY_DNS'

# S3_BUCKET_NAME_KEYNAME = 'S3_BUCKET_NAME'
# S3_BUCKET_NAME_DEFAULT = 'test-s3-bucket'

# S3_ENDPOINT_URL_KEYNAME = 'S3_ENDPOINT_URL'
# S3_ENDPOINT_URL_DEFAULT = 'https://storage.yandexcloud.net'

# RUN_TIMESTAMP_KEYNAME = 'RUN_TIMESTAMP'
# S3_ACCESS_KEY_ID_KEYNAME = 'S3_ACCESS_KEY_ID'
# S3_ACCESS_KEY_KEYNAME = 'S3_ACCESS_KEY'
# S3_CREDENTIALS_PATH_KEYNAME = 'AWS_SHARED_CREDENTIALS_FILE'
# S3_CONFIG_PATH_KEYNAME = 'AWS_CONFIG_FILE'
# S3_MAX_ATTEMPTS_KEYNAME = 'S3_MAX_ATTEMPTS'
# S3_MAX_ATTEMPTS_DEFAULT = 10

# # CACHE OPTIONS
# CACHE_OPTIONS_KEYNAME = 'CACHE'
# CACHE_STORING_KEYNAME = 'STORE'
# CACHE_STORING_DEFAULT = True
# CACHE_USE_KEYNAME = 'USE'
# CACHE_USE_DEFAULT = False

# CACHE_INVALIDATE_KEYNAME = 'INVALIDATE_BY'
# CACHE_INVALIDATE_BY_TIME_KEYNAME = 'TIME'
# CACHE_INVALIDATE_BY_TIME_DEFAULT = None
# CACHE_INVALIDATE_BY_UNCOMPLITED_KEYNAME = 'SUCCESS'
# CACHE_INVALIDATE_BY_UNCOMPLITED_DEFAULT = True
# CACHE_INVALIDATE_BY_USED_KEYNAME = 'USED_COUNT'
# CACHE_INVALIDATE_BY_BOUND_KEYNAME = 'BOUND'
# CACHE_INVALIDATE_BY_RUNTIME_KEYNAME = 'RUNTIME'
# CACHE_INVALIDATE_BY_ON_BUILD_KEYNAME = 'ON_BUILD'
# CACHE_INVALIDATE_BY_ON_ARTS_KEYNAME = 'ON_ARTS'
# CACHE_INVALIDATE_BY_ON_RUN_KEYNAME = 'ON_RUN'

# # ON ERROR
# ON_ERROR_KEYNAME = 'ON_ERROR'
# ON_ERROR_EXEC_KEYNAME = 'EXEC'
# ON_ERROR_EXEC_DEFAULT = None
# ON_ERROR_REPEAT_KEYNAME = 'REPEAT'
# ON_ERROR_REPEAT_DEFAULT = 0
# ON_ERROR_HAVE_ATTEMPTS_KEYNAME = 'attempts_count'
# ON_ERROR_PAUSE_KEYNAME = 'PAUSE'
# ON_ERROR_USED_PAUSE_KEYNAME = 'USED_PAUSE'
# ON_ERROR_PAUSE_DEFAULT = '0s'
# ON_ERROR_TIME_ERROR_KEYNAME = 'last_time'
# ON_ERROR_TOTAL_KEYNAME = 'total'
# ON_ERROR_BY_EXEC_KEYNAME = 'by_exec'


# # CONTEXT INSTRUCTIONS
# CONTEXT_KEYNAME = 'context'

# CUBE_NAME_KEYNAME = 'CUBE_NAME'  # FIXME: Кажется это внутренний ключ, надо бы их как-то иначе обозначать

# CONTEXT_GENERATORS = 'context_generator'

# ARTEFACT_INFO_REPORT_COUNT_KEYNAME = 'ARTEFACT_INFO_REPORT_COUNT'
# ARTEFACT_INFO_REPORT_COUNT_DEFAULT = 30

# COLLECT_MEM_USAGE_KEYNAME = 'COLLECT_MEM_USAGE'
# COLLECT_MEM_USAGE_DEFAULT = False


# # STEPS INSTRUCTIONS
# STEPS_KEYNAME = 'steps'
# CUBES_KEYNAME = 'cubes'
# DEPENDS_ON_KEYNAME = 'depends_on'
# TAGS_KEYNAME = 'tags'

# EXEC_KEYNAME = 'exec'
# PARAMS_KEYNAME = 'context'
# GENERATE_WITH_KEYNAME = 'generate_with'

# INDEXED_INPUTS_KEYNAME = 'inputs'
# NAMED_INPUTS_KEYNAME = 'named_inputs'
# ALL_INPUTS_KEYNAME = '*'


# # OTHER CONST

# ONECUBE_AUTO_NAME = '__cube__'
# ALL_OUTPUTS_INDEX = f'{ALL_INPUTS_KEYNAME}_indexed'
# ALL_OUTPUTS_NAMED_INDEX = f'{ALL_INPUTS_KEYNAME}_named'

# EXEC_PATH_SEPARATOR = ':'
# TAG_EXP_START = '@'

# DAG_SEPARATOR = ':'
# CUBE_SEPARATOR = '.'
# INDEX_SEPARATOR = '['
# INDEX_FINISHER = ']'
# LIST_SEPARATOR = ','
# OUTPUT_OPTION_SEPARATOR = '^'
# OUTPUT_OPTION_NOT_ONLY_SUCCESS = 'not_only_success'
# OUTPUT_OPTION_NOT_ONLY_SUCCESS_DEFAULT = False
# OUTPUT_OPTION_MIN_DATE = 'min_date'
# OUTPUT_OPTION_MIN_DATE_DEFAULT = None
# OUTPUT_OPTION_MAX_DATE = 'max_date'
# OUTPUT_OPTION_MAX_DATE_DEFAULT = None
# OUTPUT_OPTION_COUNT_RUNS = 'count_runs'
# OUTPUT_OPTION_COUNT_RUNS_DEFAULT = -1
# OUTPUT_OPTION_COUNT_RUNS_INF = '*'

# INTERSECT_SET_OPERATOR = '&'
# UNITE_SET_OPERATOR = '|'
# DIFF_SET_OPERATOR = '-'
# SYM_DIFF_SET_OPERATOR = '^'
# # NOT_SET_OPERATOR = '^'