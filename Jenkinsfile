import groovy.json.JsonSlurper
class status
{ 
     String description
     String event_handler
     String[] host_groups
     String host_name
}

properties([
    [
        $class: 'JiraProjectProperty'
    ], 
    
    parameters([
        
        [
            
            $class: 'ExtensibleChoiceParameterDefinition', 
            choiceListProvider: [$class: 'TextareaChoiceListProvider',
            addEditedValue: false,
            choiceListText: '''DoNothing\nEnable\nDisable''',
            defaultChoice: 'DoNothing'],
            description: '',
            editable: false,
            name: 'JobAction'
            
        ],
        
        [
            
            $class: 'CascadeChoiceParameter',
            choiceType: 'PT_CHECKBOX', 
            description: '', 
            filterLength: 1, 
            filterable: false, 
            name: 'JobName', 
            randomName: 'choice-parameter-38182946397479', 
            referencedParameters: 'JobAction', 
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], 
                sandbox: false, 
                script: ''], 
                script: [classpath: [], 
                sandbox: false, 
                script: '''if (JobAction.equals("Enable") || JobAction.equals("Disable")) {\nreturn ["NF_PRO_Indexing_Automation","NF_PRO_Re-Indexing","F_PROD_Re-Indexing","StoreFront_Restart_On_AjpRejectedCount","Food_StoreFront_Restart_On_AjpRejectedCount"]\n}''']
                ]
                
        ],
        
        [
            $class: 'ExtensibleChoiceParameterDefinition',
            choiceListProvider: [$class: 'TextareaChoiceListProvider', 
            addEditedValue: false, 
            choiceListText: '''DoNothing\nEnable\nDisable''',
            defaultChoice: 'Enable'], 
            description: '', 
            editable: false, 
            name: 'EventHandlerAction'
        ],
        
        [
            $class: 'CascadeChoiceParameter', 
            choiceType: 'PT_CHECKBOX', 
            description: '', 
            filterLength: 1, 
            filterable: false, 
            name: 'ServiceName', 
            randomName: 'choice-parameter-38182949408198', 
            referencedParameters: 'EventHandlerAction', 
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], 
                sandbox: false, script: ''], 
                script: [classpath: [], 
                sandbox: false, 
                script: '''if (EventHandlerAction.equals("Enable") || EventHandlerAction.equals("Disable")) {\nreturn ["check_jboss_gc","check_ajp_avg_request_rejected_count","check_ATGProductionDS_session_count","check_mdex_load_restartWA"]\n}''']
                
            ]
        ],
         
        [
            $class: 'CascadeChoiceParameter', 
            choiceType: 'PT_CHECKBOX', 
            description: '', 
            filterLength: 1, 
            filterable: false, 
            name: 'Call_automation_Non_food', 
            randomName: 'choice-parameter-38182959006666', 
            referencedParameters: 'EventHandlerAction', 
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], 
                sandbox: false, 
                script: ''], 
                script: [classpath: [], 
                sandbox: false, 
                script: '''if (EventHandlerAction.equals("Enable") || EventHandlerAction.equals("Disable")) {\nreturn ["check_pod_restartcount_nonbusiness_ms_esb_product_provider","check_atuin_CC_Confirmed_ordercount","check_atuin_CC_Confirmed_ordercount_WeekEnd","check_atuin_CC_Integrated_ordercount","check_atuin_CC_Issued_ordercount","check_atuin_CC_Preparing_ordercount","check_atuin_CC_Reserved_ordercount","check_atuin_Textile_confirmed_ordercount","check_atuin_Textile_confirmed_ordercount_WeekEnd","check_atuin_Textile_issued_ordercount","check_atuin_Textile_preparing_ordercount","check_atuin_Textile_reserved_ordercount","check_atuin_almacen_cancelled_ordercount","check_atuin_almacen_error_ordercount","check_atuin_almacen_integrated_ordercount","check_atuin_almacen_invoiced_ordercount","check_atuin_almacen_issued_ordercount","check_atuin_almacen_preparing_ordercount","check_atuin_almacen_reserved_ordercount","check_atuin_orders_cancelled_after_checkout","check_atuin_textile_integrated_ordercount","atuin-prod-order-status-update_lag","atuin-prod-payment-status-update_lag","atuin-prod-product-volumetry_lag"]\n}''']
            ]
        ], 
        
        [
            $class: 'CascadeChoiceParameter', 
            choiceType: 'PT_CHECKBOX', 
            description: '', 
            filterLength: 1, 
            filterable: false, 
            name: 'C4Environment', 
            randomName: 'choice-parameter-38182959825985', 
            referencedParameters: 'EventHandlerAction',
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], 
                sandbox: false, 
                script: ''], 
                script: [classpath: [], 
                sandbox: false, 
                script: '''if (EventHandlerAction.equals("Enable") || EventHandlerAction.equals("Disable")) {\nreturn ["FOOD-PRODUCTION","NONFOOD-PRODUCTION","ATUIN-Microservices-PROD"]\n}''']
            ]
            
        ], 
        
        [
            $class: 'CascadeChoiceParameter', 
            choiceType: 'PT_RADIO', 
            description: '', 
            filterLength: 1, 
            filterable: false, 
            name: 'EventHandler', 
            randomName: 'choice-parameter-38182962295796', 
            referencedParameters: 'ServiceName,Call_automation_Non_food,C4Environment', 
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], 
                sandbox: false, 
                script: ''], 
                script: [classpath: [], 
                sandbox: false, 
                script: 'return ["sf_restart","ATUIN_OrderCount_Escalations","check_ds_session","mdex_load_eventhandler"]']
                
                ]
        ],
        
        [
            $class: 'CascadeChoiceParameter', 
            choiceType: 'PT_RADIO', 
            description: '', filterLength: 1, 
            filterable: false, 
            name: 'BotsExcluded', 
            randomName: 'choice-parameter-38182989621050', 
            referencedParameters: 'ServiceName', 
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], 
                sandbox: false, 
                script: ''], 
                script: [classpath: [], 
                sandbox: false, 
                script: 'return ["YES:selected"]']
                ]
        ]
    ])
])


node() {



    stage('Build') { 
        List servers = "${C4Environment}".split(',')

        sh "status=\$(curl -s --insecure -u 'omdguest:omdguest' -H 'Accept:application/json' -k -L 'http://omd.carrefour.es/c4omd/thruk/cgi-bin/status.cgi?view_mode=json&s0_op=%3D&s0_type=event+handler&s0_value=sf_restart&columns=host_name,description,event_handler,host_groups')" 
        
        println(status[0].description)


        def slurper = new JsonSlurper()

        def jsonMap = slurper.parseText(status)
        def statusObject = new status(jsonMap)
        println(statusObject.host_name)
        //def hostname = json.host_name
            

    

    }

        




}