properties([
    
    
    [
        $class: 'JiraProjectProperty'
        
    ],
    
    
    parameters([
        
        
        
        [
            
            $class: 'ExtensibleChoiceParameterDefinition',
            choiceListProvider: [$class: 'TextareaChoiceListProvider',
            addEditedValue: false,
            choiceListText: '''DoNothing
            Enable
            Disable
            ''', 
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
          randomName: 'choice-parameter-32567460212416', 
          referencedParameters: 'JobAction', 
          script: [
              $class: 'GroovyScript', 
              fallbackScript: [classpath: [],
              sandbox: false, 
              script: ''],
              script: [classpath: [], 
              sandbox: false, 
              script: '''if (JobAction.equals("Enable") || JobAction.equals("Disable")) {
                         return ["NF_PRO_Indexing_Automation","NF_PRO_Re-Indexing","F_PROD_Re-Indexing","StoreFront_Restart_On_AjpRejectedCount","Food_StoreFront_Restart_On_AjpRejectedCount"]
                        }''']
                        
            ]


        ]


    ])




])