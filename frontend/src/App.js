import React, { useState, useEffect } from "react"
import axios from 'axios'

import { Box, Stack, VStack, HStack, Flex, Text } from '@chakra-ui/react'

import {ContextSocketProvider} from './context/context-socketio'
import Form from "./components/Form"

const App = () => {

    return(
        <ContextSocketProvider>
            <Box>
                <Text>Hola</Text>
                <Form />
            </Box>
        </ContextSocketProvider>
    )
}

export default App