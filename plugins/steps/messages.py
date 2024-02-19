from airflow.providers.telegram.hooks.telegram import TelegramHook


def send_telegram_success_message(context):
    hook = TelegramHook(telegram_conn_id='test',
                                                token='7147789729:AAHM1bHjv3bytImyjjg6FuDcXNE9aBY5544',
                                                chat_id='4168166035')
    
    dag = context['dag']
    run_id = context['run_id']

    message = f'Исполненение DAG {dag} с id={run_id} прошло успешно!'
    hook.send_message({
        'chat_id': '4168166035',
        'text': message
    })

def send_telegram_failure_message(context):
    hook = TelegramHook(telegram_conn_id='test',
                        token='7147789729:AAHM1bHjv3bytImyjjg6FuDcXNE9aBY5544',
                        chat_id='4168166035')
    
    dag_info = context['task_instance_key_str']
    run_id = context['run_id']

    message = f'DAG {dag_info} с номером запуска run_id={run_id} завершился с ошибкой.'
    hook.send_message({
        'chat_id': '4168166035',
        'text': message
    })
