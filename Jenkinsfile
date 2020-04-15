properties([
  [
      $class: 'JiraProjectProperty'
  ],
  
  parameters([
        [
          $class: 'ExtensibleChoiceParameterDefinition',
          choiceListProvider: [$class: 'TextareaChoiceListProvider',
          addEditedValue: false, choiceListText: '''1
          2
          3
          ''',
          defaultChoice: '1'],
          description: '',
          editable: false,
          name: 'test'
        ],

        [
            $class: 'CascadeChoiceParameter',
            choiceType: 'PT_CHECKBOX',
            description: '',
            filterLength: 1,
            filterable: false,
            name: 'JobName',
            randomName: 'choice-parameter-29693612935685',
            referencedParameters: 'JobAction',
            script: [
                $class: 'GroovyScript',
                fallbackScript: [
                 classpath: [],
                 sandbox: false,
                 script: ''
                ],

                script: [
                 classpath: [],
                 sandbox: false,
                 script: '''if (JobAction.equals("Enable") || JobAction.equals("Disable")) {
                 return ["NF_PRO_Indexing_Automation","NF_PRO_Re-Indexing","F_PROD_Re-Indexing","StoreFront_Restart_On_AjpRejectedCount","Food_StoreFront_Restart_On_AjpRejectedCount"]
                 }'''
                ]
            ]
             











        ]

    


    ]
)])


